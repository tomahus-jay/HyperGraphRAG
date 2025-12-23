"""Pydantic models for type safety and validation"""
from typing import List, Dict, Any, Optional
from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime


class EntityType(str, Enum):
    """Entity type enumeration"""
    PERSON = "PERSON"
    ORGANIZATION = "ORGANIZATION"
    CONCEPT = "CONCEPT"
    TECHNOLOGY = "TECHNOLOGY"
    EVENT = "EVENT"
    LOCATION = "LOCATION"
    PRODUCT = "PRODUCT"
    OTHER = "OTHER"


class Entity(BaseModel):
    """Entity model"""
    name: str = Field(..., description="Entity name")
    type: EntityType = Field(..., description="Entity type")
    description: Optional[str] = Field(None, description="Entity description in context")
    
    class Config:
        use_enum_values = True


class Hyperedge(BaseModel):
    """Hyperedge model - connects multiple entities with shared knowledge"""
    entity_names: List[str] = Field(..., description="List of entity names connected by this hyperedge")
    content: str = Field(..., description="Knowledge content shared by these entities")
    hyperedge_id: Optional[str] = Field(None, description="Unique hyperedge identifier")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")
    
    class Config:
        use_enum_values = True
    
    def __hash__(self):
        """Make hyperedge hashable for set operations"""
        return hash((tuple(sorted(self.entity_names)), self.content))


class ExtractedHyperedge(BaseModel):
    """
    Strict Hyperedge model for LLM extraction (Structured Outputs).
    Excludes fields like 'metadata' (Dict[str, Any]) which are not compatible with strict schemas.
    """
    entity_names: List[str] = Field(..., description="List of entity names connected by this hyperedge")
    content: str = Field(..., description="Knowledge content shared by these entities")
    
    class Config:
        use_enum_values = True


class ChunkMetadata(BaseModel):
    """Chunk metadata model"""
    document_index: Optional[int] = Field(None, description="Index of the document this chunk belongs to")
    chunk_index: Optional[int] = Field(None, description="Index of the chunk within the document")
    start_idx: Optional[int] = Field(None, description="Start index in the original document")
    end_idx: Optional[int] = Field(None, description="End index in the original document")
    source: Optional[str] = Field(None, description="Source of the document")
    category: Optional[str] = Field(None, description="Category of the document")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")
    
    class Config:
        extra = "allow"  # Allow additional fields


class Chunk(BaseModel):
    """Chunk model"""
    id: str = Field(..., description="Unique chunk identifier")
    content: str = Field(..., description="Chunk content")
    metadata: ChunkMetadata = Field(..., description="Chunk metadata")
    entities: Optional[List[str]] = Field(None, description="List of entity names mentioned in this chunk")
    
    class Config:
        extra = "allow"


class ChunkSearchResult(BaseModel):
    """Chunk search result model"""
    chunk_id: str = Field(..., description="Chunk identifier")
    content: str = Field(..., description="Chunk content")
    score: float = Field(..., description="Similarity score")
    entities: List[str] = Field(default_factory=list, description="Entities mentioned in this chunk")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Chunk metadata")


class HyperedgeInfo(BaseModel):
    """Hyperedge information model"""
    hyperedge_id: str = Field(..., description="Hyperedge identifier")
    entities: List[str] = Field(..., description="Entities connected by this hyperedge")
    content: str = Field(..., description="Knowledge content")


class QueryResult(BaseModel):
    """Query search result model"""
    query: str = Field(..., description="Original query text")
    top_chunks: List[ChunkSearchResult] = Field(default_factory=list, description="Top matching chunks")
    hyperedges: List[HyperedgeInfo] = Field(default_factory=list, description="Related hyperedges")
    expanded_chunks: List[Dict[str, Any]] = Field(default_factory=list, description="Expanded chunks from graph")
    total_chunks_found: int = Field(0, description="Total number of chunks found")
    total_hyperedges_found: int = Field(0, description="Total number of hyperedges found")
    total_expanded_chunks: int = Field(0, description="Total number of expanded chunks")
    entities_found: List[str] = Field(default_factory=list, description="All entities found in results")


class GraphExtractionResult(BaseModel):
    """Result of graph extraction containing entities and hyperedges"""
    entities: List[Entity] = Field(..., description="List of extracted entities")
    hyperedges: List[ExtractedHyperedge] = Field(..., description="List of extracted hyperedges")
