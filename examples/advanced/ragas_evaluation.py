import asyncio
import os
import warnings
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Filter multiprocessing resource tracker warning
warnings.filterwarnings("ignore", message=".*resource_tracker.*")

import pandas as pd
from datasets import load_dataset
from ragas import evaluate
from ragas.metrics import context_recall, context_precision
from hypergraphrag import HyperGraphRAG

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------
SAMPLE_SIZE = 1000
TOP_K = 5
MAX_HOPS = 2

async def main():
    print("🚀 Starting HotpotQA Evaluation with Ragas...")
    
    # 1. Load HotpotQA Dataset
    print("📦 Loading HotpotQA dataset (distractor)...")
    dataset = load_dataset("hotpot_qa", "distractor", split="validation")
    
    # Select a subset
    subset = dataset.select(range(SAMPLE_SIZE))
    print(f"📊 Evaluated samples: {len(subset)}")
    
    # 2. Bulk Insert Data (Simulate realistic retrieval environment)
    # print("preparing documents for bulk insert...")
    # all_documents = []
    # all_metadatas = []
    # seen_titles = set()

    # Collect ALL contexts from the subset
    # for sample in subset:
    #     context = sample["context"] # {'title': [], 'sentences': []}
    #     for title, sentences in zip(context["title"], context["sentences"]):
    #         if title not in seen_titles:
    #             doc_content = f"{title}\n" + " ".join(sentences)
    #             all_documents.append(doc_content)
    #             all_metadatas.append({"title": title, "source": "hotpot_qa"})
    #             seen_titles.add(title)
    
    # print(f"📝 Bulk Inserting {len(all_documents)} unique documents...")
    
    # Initialize RAG Client (Will use .env settings for model)
    rag = HyperGraphRAG(
        chunk_size=768,
        chunk_overlap=50,
        llm_request_timeout=300.0  # Increase timeout to 5 minutes to avoid timeouts
    )
    
    try:
        # Reset DB once
        # rag.reset_database()
        
        # Bulk Insert
        # Lower concurrency to avoid overloading the LLM server/API
        # await rag.add(
        #     documents=all_documents, 
        #     metadata=all_metadatas,
        #     batch_size=5,
        #     max_concurrent_tasks=10
        # )
        
        # 3. Query & Collect Results
        print("🔍 Querying and collecting results...")
        ragas_data = {
            "question": [],
            "contexts": [],
            "ground_truth": []
        }
        
        for i, sample in enumerate(subset):
            question = sample["question"]
            supporting_facts = sample["supporting_facts"]
            context = sample["context"]
            
            # Prepare Ground Truth Sentences
            ground_truth_sentences = []
            context_map = dict(zip(context["title"], context["sentences"]))
            
            for title, sent_id in zip(supporting_facts["title"], supporting_facts["sent_id"]):
                if title in context_map and sent_id < len(context_map[title]):
                    ground_truth_sentences.append(context_map[title][sent_id])
            
            if not ground_truth_sentences:
                continue

            # Retrieval
            result = await rag.query_local(
                query_text=question,
                top_n=TOP_K,
                max_hops=MAX_HOPS
            )
            
            retrieved_contexts = [chunk.content for chunk in result.top_chunks]
            
            ragas_data["question"].append(question)
            ragas_data["contexts"].append(retrieved_contexts)
            ragas_data["ground_truth"].append(ground_truth_sentences)
            
            if (i+1) % 5 == 0:
                print(f"   Processed {i+1}/{SAMPLE_SIZE} queries...")

    finally:
        rag.close()
        
    # 4. Run Ragas Evaluation
    print("\n🤖 Running Ragas Evaluation...")
    
    # Create Dataset
    df = pd.DataFrame(ragas_data)
    # Join ground truths for Ragas compatibility
    df["ground_truth"] = df["ground_truth"].apply(lambda x: "\n".join(x))
    
    from datasets import Dataset
    ragas_dataset = Dataset.from_pandas(df)
    
    # Run evaluation
    results = evaluate(
        ragas_dataset,
        metrics=[
            context_recall,
            context_precision,
        ],
    )
    
    print("\n" + "="*50)
    print("🏆 Ragas Evaluation Results")
    print("="*50)
    print(results)
    
    # Detailed view
    print("\n📄 Detailed Results per Sample:")
    res_df = results.to_pandas()
    
    # Ragas might rename 'question' to 'user_input' or just return metrics
    question_col = "question"
    if "question" not in res_df.columns and "user_input" in res_df.columns:
        question_col = "user_input"
        
    cols_to_show = [question_col, 'context_recall', 'context_precision']
    # Filter only existing columns just in case
    cols_to_show = [c for c in cols_to_show if c in res_df.columns]
    
    print(res_df[cols_to_show])

if __name__ == "__main__":
    asyncio.run(main())
