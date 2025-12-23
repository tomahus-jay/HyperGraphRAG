"""Pytest configuration and fixtures"""
import pytest
from typing import Generator
from hypergraphrag import HyperGraphRAG


@pytest.fixture
def mock_rag_client() -> Generator[HyperGraphRAG, None, None]:
    """Create a mock RAG client for testing"""
    # This would be configured with test databases
    # For now, it's a placeholder
    yield None


