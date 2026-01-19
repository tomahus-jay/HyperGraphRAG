"""Tests for Pydantic models"""
import pytest
from hypergraphrag.models import (
    Entity,
    Hyperedge,
    ChunkMetadata,
    Chunk,
    QueryResult
)


def test_entity_model():
    """Test Entity model"""
    entity = Entity(
        name="Artificial Intelligence",
        description="A field of computer science"
    )
    assert entity.name == "Artificial Intelligence"
    assert entity.description == "A field of computer science"


def test_hyperedge_model():
    """Test Hyperedge model"""
    hyperedge = Hyperedge(
        entity_names=["AI", "Machine Learning"],
        content="Machine Learning is a subset of AI",
        chunk_id="chunk_1"
    )
    assert len(hyperedge.entity_names) == 2
    assert hyperedge.content == "Machine Learning is a subset of AI"
    assert hyperedge.chunk_id == "chunk_1"


def test_chunk_metadata_model():
    """Test ChunkMetadata model"""
    metadata = ChunkMetadata(
        document_index=0,
        chunk_index=1,
        start_idx=0,
        end_idx=100,
        source="test_doc",
        category="test"
    )
    assert metadata.document_index == 0
    assert metadata.chunk_index == 1


def test_query_result_model():
    """Test QueryResult model"""
    result = QueryResult(
        query="test query",
        hyperedges=[]
    )
    assert result.query == "test query"
    assert result.hyperedges == []


