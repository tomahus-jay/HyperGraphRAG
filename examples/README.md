# Hypergraph RAG Examples

This directory contains example scripts demonstrating how to use Hypergraph RAG, organized by complexity and use case.

## 📂 1. Basics (`examples/basics/`)
Getting started with core functionalities.

- **`01_add_documents.py`**: Adds documents to the Hypergraph RAG system.
  - *Usage:* `python examples/basics/01_add_documents.py`
- **`02_query_documents.py`**: Performs search queries on the indexed data.
  - *Usage:* `python examples/basics/02_query_documents.py`
- **`03_e2e_demo.py`**: A complete end-to-end example (Add + Query).
  - *Usage:* `python examples/basics/03_e2e_demo.py`

## 🚀 2. Advanced (`examples/advanced/`)
Advanced features like streaming and evaluation.

- **`stream_add.py`**: Adds documents using a streaming interface for real-time progress updates.
  - *Usage:* `python examples/advanced/stream_add.py`
- **`ragas_evaluation.py`**: Evaluates the RAG system using the Ragas framework with HotpotQA dataset.
  - *Usage:* `python examples/advanced/ragas_evaluation.py`

## 🛠️ 3. Utils (`examples/utils/`)
Utility scripts for maintenance and debugging.

- **`check_health.py`**: Checks the connection status of Neo4j and vector indices.
  - *Usage:* `python examples/utils/check_health.py`

## Prerequisites

Make sure you have your environment variables set up (see main [README.md](../README.md)) before running these examples.
