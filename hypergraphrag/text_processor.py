"""Text preprocessing and chunking utility"""
from typing import List, Dict, Any
import hashlib


class TextProcessor:
    """Text processing and chunking"""
    
    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 500,
        chunk_overlap: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Split text into chunks
        
        Args:
            text: Text to split
            chunk_size: Maximum size of each chunk (character count)
            chunk_overlap: Number of overlapping characters between chunks
        
        Returns:
            List of chunks (each chunk contains id, content, start_idx, end_idx)
        """
        chunks = []
        start = 0
        chunk_id = 0
        
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]
            
            if chunk_text.strip():  # Exclude empty chunks
                chunk_id_str = hashlib.md5(
                    f"{chunk_text}_{start}_{end}".encode()
                ).hexdigest()
                
                chunks.append({
                    "id": chunk_id_str,
                    "content": chunk_text,
                    "start_idx": start,
                    "end_idx": end,
                    "chunk_index": chunk_id
                })
            
            start = end - chunk_overlap
            chunk_id += 1
        
        return chunks

