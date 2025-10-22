from pathlib import Path
from src.llm import LLM
from src.chatbot import ChatBot
from src.vector_database import VectorDDBB

def ejercicio1(llm: LLM):
    """Ejercicio 1: conexión básica con OpenAI"""
    system_msg = "You are a helpful assistant."
    user_msg = "How many 'a' are in the word 'MasOrange'?"
    response = llm.call(system_msg, user_msg)
    print(response)


def ejercicio2_1(llm: LLM):
    """Ejercicio 2.1: generación de embedding básica"""
    vec2 = llm.get_embedding("You shall not pass!")
    print(vec2)
    print(f"Embedding length: {len(vec2)}")


def ejercicio2_2():
    """Ejercicio 2.2: creación de la base de datos vectorial"""
    vector_db = VectorDDBB()

    sample_markdown = """
    # Introduction
    This is the introduction section.
    
    ## First Section
    This is the first section with some content.
    
    ## Second Section
    This is the second section with different content.
    
    ## Third Section
    And this is the third section.
    """
    vector_db.load_document(sample_markdown)
    vector_db.print_number_of_embeddings()


def ejercicio3():
    """Ejercicio 3: búsqueda de chunks similares"""
    # Create instance
    vector_db = VectorDDBB()
    # Load document and create embeddings
    md_path = Path(__file__).parent.parent / "ai-engineer-evaluation-test.md"
    vector_db.load_document_from_path(md_path)
    # Print number of embeddings
    vector_db.print_number_of_embeddings()
    # Find nearest chunk
    nearest_chunk = vector_db.nearest_chunks("Darle funcionalidad a la base de datos")[0]
    print(nearest_chunk)


def ejercicio4():
    """Ejercicio 4: integración completa del ChatBot"""
    # Create LLM and VectorDB instances
    vector_db = VectorDDBB()
    # Load document and create embeddings
    md_path = Path(__file__).parent.parent / "ai-engineer-evaluation-test.md"
    vector_db.load_document_from_path(md_path)
    # Create ChatBot instance
    chatbot = ChatBot(vector_db)
    # Lista de preguntas
    questions = [
        "¿Cuál es la pregunta que se debe responder en el ejercicio 1: Tu primera conexión IA?",
        "¿Cuáles son los Bonus Points generales que engloban todo el proceso?",
        "¿Qué modelos hay disponibles para el uso en el ejercicio?"
    ]
    for question in questions:
        answer = chatbot.answer_question(question)
        print(f"Q: {question}\nA: {answer}")
        print()


def main():
    ejercicio4()


if __name__ == "__main__":
    main()