# Contributing to Hypergraph RAG

Thank you for your interest in contributing to Hypergraph RAG!

## Development Setup

1. Clone the repository
2. Install dependencies using uv:
   ```bash
   uv sync --dev
   ```

3. Set up environment variables (create `.env` file):
   ```
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USER=neo4j
   NEO4J_PASSWORD=your_password
   QDRANT_URL=http://localhost:6333
   OPENAI_API_KEY=your_api_key
   ```

## Code Style

- Use `black` for code formatting
- Use `ruff` for linting
- Follow PEP 8 style guide
- Type hints are encouraged

## Running Tests

```bash
pytest
```

With coverage:
```bash
pytest --cov=hypergraphrag --cov-report=html
```

## Submitting Changes

1. Create a feature branch
2. Make your changes
3. Add tests if applicable
4. Ensure all tests pass
5. Submit a pull request


