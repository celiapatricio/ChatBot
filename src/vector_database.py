from src.llm import LLM
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
