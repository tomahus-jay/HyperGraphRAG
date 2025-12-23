"""Tests for Pydantic models"""
import pytest
from hypergraphrag.models import (
    Entity,
    Hyperedge,
    EntityType,
    RelationshipType,
    ChunkMetadata,
    Chunk,
    ChunkSearchResult,
    HyperedgeInfo,
    QueryResult
)


def test_entity_model():
    """Test Entity model"""
    entity = Entity(
        name="Artificial Intelligence",
        type=EntityType.CONCEPT,
        description="A field of computer science"
    )
    assert entity.name == "Artificial Intelligence"
    assert entity.type == EntityType.CONCEPT
    assert entity.description == "A field of computer science"


def test_hyperedge_model():
    """Test Hyperedge model"""
    hyperedge = Hyperedge(
        entity_names=["AI", "Machine Learning"],
        relationship="Machine Learning is a subset of AI",
        type=RelationshipType.PART_OF
    )
    assert len(hyperedge.entity_names) >= 2
    assert hyperedge.type == RelationshipType.PART_OF


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
        query_entities=["AI"],
        top_chunks=[],
        hyperedges=[],
        expanded_chunks=[],
        total_chunks_found=0,
        total_hyperedges_found=0,
        total_expanded_chunks=0,
        entities_found=[]
    )
    assert result.query == "test query"
    assert result.total_chunks_found == 0


