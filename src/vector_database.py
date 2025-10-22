from src.llm import LLM
from pathlib import Path
from abc import ABC, abstractmethod


class VectorDatabaseInterface(ABC):
    """
    Abstract interface for vector database implementations.
    
    Expected constructor signature:
        __init__(self) -> None
            Should initialize:
            - self.client: openai.OpenAI client
            - self.embeddings: List for storing embeddings
            - self.chunks: List for storing text chunks
    """
    
    @abstractmethod
    def load_document(self, markdown_text: str) -> None:
        """Load and process a document into embeddings."""
        pass
    
    @abstractmethod
    def print_number_of_embeddings(self) -> None:
        """Print the number of stored embeddings."""
        pass

    @abstractmethod
    def load_document_from_path(self, markdown_path: Path) -> None:
        """Load and process a document into embeddings."""
        pass


class VectorDDBB(VectorDatabaseInterface):
    def __init__(self):
        self.llm = LLM()
        self.embeddings = []
        self.chunks = []
    
    def load_document(self, markdown_text: str) -> None:
        split_chunks = markdown_text.split("##")
        i = 0
        for chunk in split_chunks:
            chunk = chunk.strip()
            self.chunks.append(chunk)
            vector = self.llm.get_embedding(chunk)
            self.embeddings.append(vector)
            i += 1

    def print_number_of_embeddings(self) -> None:
        print(f"Number of embeddings stored: {len(self.embeddings)}")

    def _nearest_chunks(self, embedding: list[int], top_n: int = 3) -> list[str]:
        """Return the nearest chunks to the given embedding with the dot product similarity"""
        # Calculate dot product similarity for each stored embedding
        similarities = []
        for i, stored_embedding in enumerate(self.embeddings):
            dot_product = sum(a * b for a, b in zip(embedding, stored_embedding))
            similarities.append((dot_product, i))
        
        similarities.sort(reverse=True, key=lambda x: x[0])
        
        return [self.chunks[i] for _, i in similarities[:top_n]]

    def nearest_chunks(self, text: str) -> list[str]:
        if not self.embeddings:
            return []
        emb = self.llm.get_embedding(text)
        return self._nearest_chunks(emb)

    def load_document_from_path(self, markdown_path: Path) -> None:
        with open(markdown_path, 'r', encoding='utf-8') as file:
            markdown_text = file.read()
        self.load_document(markdown_text)
