# Examples

This directory contains example scripts demonstrating how to use Hypergraph RAG.

## Basic Usage

`basic_usage.py` - A simple example showing how to:
- Initialize the Hypergraph RAG client
- Insert documents
- Query the knowledge base
- Display results

Run with:
```bash
python examples/basic_usage.py
```

## Insert Only

`insert_only.py` - Example for inserting documents only:
- Initialize the Hypergraph RAG client
- Insert multiple documents with metadata
- Configure batch processing options
- Display insertion status

Run with:
```bash
python examples/insert_only.py
```

## Query Only

`query_only.py` - Example for querying only (assumes data is already inserted):
- Initialize the Hypergraph RAG client
- Perform multiple queries
- Display search results including chunks, hyperedges, and entities
- Show similarity scores and relationships

Run with:
```bash
python examples/query_only.py
```

## Self-Hosted LLM

`self_hosted_llm.py` - Example for using self-hosted LLM services:
- Configure LM Studio, vLLM, Ollama, or other OpenAI-compatible servers
- Set up custom LLM endpoints using `base_url`

## Self-Hosted Embeddings

`self_hosted_embeddings.py` - Example for using self-hosted embedding services:
- Configure custom embedding servers
- Use HTTP-based embedding endpoints using `base_url`

## Prerequisites

Make sure you have:
- Neo4j running and configured
- Qdrant running and configured
- LLM API key or self-hosted LLM server configured
- Embedding provider configured (if using API-based embeddings)

See the main [README.md](../README.md) for detailed configuration instructions.

