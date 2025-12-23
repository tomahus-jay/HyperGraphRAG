"""LLM prompts for graph extraction"""

GRAPH_EXTRACTION_SYSTEM_PROMPT = """You are an expert Knowledge Graph Engineer.
Your goal is to analyze the text and extract a dense knowledge graph consisting of Entities and Hyperedges (facts connecting entities)."""

GRAPH_EXTRACTION_USER_PROMPT_TEMPLATE = """Analyze the following text and extract **Entities** and **Hyperedges** (Atomic Facts).

**1. Entity Extraction Rules:**
- Extract key entities: People, Organizations, Locations, Events, Dates, Concepts, etc.
- Use **Canonical Names** (e.g., "United States" instead of "US").
- Resolve pronouns to their full entity names.

**2. Hyperedge (Fact) Extraction Rules:**
- A Hyperedge represents a **unit of knowledge** connecting multiple entities.
- **Content:** A self-contained sentence explaining the fact.
- **No Pronouns:** Use full entity names in the content.
- **N-ary:** Connect 2 or more entities.

**Example Input:**
"Elon Musk founded SpaceX in 2002 with the goal of reducing space transportation costs."

**Example Extraction:**
- Entities:
  - "Elon Musk" (PERSON): Entrepreneur and founder of SpaceX
  - "SpaceX" (ORGANIZATION): Aerospace manufacturer founded by Elon Musk
  - "2002" (DATE): Year SpaceX was founded
- Hyperedges:
  - ["Elon Musk", "SpaceX", "2002"]: "Elon Musk founded SpaceX in 2002."
  - ["SpaceX", "Elon Musk"]: "SpaceX was founded by Elon Musk with the goal of reducing space transportation costs."

**Text:**
{text}
"""
