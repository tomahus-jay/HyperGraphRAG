"""Example: Check Health Status of Hypergraph RAG Connection"""
import asyncio
from hypergraphrag import HyperGraphRAG

async def main():
    print("🏥 Checking Hypergraph RAG Health Status...")
    
    # Initialize client (will try to connect to Neo4j)
    # Ensure you have your environment variables set for NEO4J and LLM/Embedding API keys
    rag = HyperGraphRAG()
    
    # Check health
    status = rag.check_health()
    
    print("\n--- Health Check Results ---")
    
    if status["healthy"]:
        print("✅ System is Healthy!")
        print(f"   Message: {status['messages'][0]}")
    else:
        print("❌ System Health Check Failed!")
        for msg in status["messages"]:
            print(f"   ⚠️  {msg}")
            
    # Print details
    print("\n--- Connection Details ---")
    details = status["details"]
    print(f"🔌 Connected: {details.get('connected')}")
    
    if details.get("indexes"):
        print("📊 Vector Indexes Found:")
        for name, dim in details["indexes"].items():
            print(f"   - {name}: {dim} dimensions")
            
    if details.get("errors"):
        print("\n🐛 Errors Encountered:")
        for err in details["errors"]:
            print(f"   - {err}")
    
    print("\n---------------------------")

    # Clean up resources
    rag.close()

if __name__ == "__main__":
    asyncio.run(main())

