import sys
from pathlib import Path
from src.llm import LLM
from src.chatbot import ChatBot
from src.vector_database import VectorDDBB

def ejercicio1(llm: LLM):
    """Ejercicio 1: conexión básica con OpenAI"""
    print("Ejercicio 1: conexión básica con OpenAI")
    system_msg = "You are a helpful assistant."
    user_msg = "How many 'a' are in the word 'MasOrange'?"
    response = llm.call(system_msg, user_msg)
    print(response)


def ejercicio2_1(llm: LLM):
    """Ejercicio 2.1: generación de embedding básica"""
    print("Ejercicio 2: sistema de embeddings")
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
    print("Ejercicio 3: búsqueda de chunks similares")
    # Create instance
    vector_db = VectorDDBB()
    # Load document and create embeddings
    md_path = Path(__file__).parent / "data" / "ai-engineer-evaluation-test.md"
    vector_db.load_document_from_path(md_path)
    # Print number of embeddings
    vector_db.print_number_of_embeddings()
    # Find nearest chunk
    nearest_chunk = vector_db.nearest_chunks("Darle funcionalidad a la base de datos")[0]
    print(nearest_chunk)


def ejercicio4():
    """Ejercicio 4: integración completa del ChatBot"""
    print("Ejercicio 4: integración completa del ChatBot")
    # Create LLM and VectorDB instances
    vector_db = VectorDDBB()
    # Load document and create embeddings
    md_path = Path(__file__).parent / "data" / "ai-engineer-evaluation-test.md"
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


def interfaz_chatbot():
    """Interfaz sencilla para el ChatBot"""
    print("Interfaz del ChatBot.")
    print("Escribe 'q' para salir.")
    vector_db = VectorDDBB()
    md_path = Path(__file__).parent / "data" / "ai-engineer-evaluation-test.md"
    vector_db.load_document_from_path(md_path)
    chatbot = ChatBot(vector_db)
    while True:
        question = input("Inserte una pregunta: ")
        if question.lower() == 'q':
            print("ChatBot finalizado. ¡Hasta luego!")
            break
        answer = chatbot.answer_question(question)
        print(f"Respuesta: {answer}")
        print("-" * 60)
        print()


def main(num: int | None = None) -> None:
    print("=" * 60)
    print("🤖 Evaluación de AI Engineer — Script principal")
    print("=" * 60)

    llm = LLM()
    if num == 1:
        ejercicio1(llm)
    elif num == 2:
        ejercicio2_1(llm)
        ejercicio2_2()
    elif num == 3:
        ejercicio3()
    elif num == 4:
        ejercicio4()
    elif num == 5:
        # Ejecutar el chatbot interfaz
        interfaz_chatbot()
    else:
        ejercicio1(llm)
        print("-" * 60)
        ejercicio2_1(llm)
        ejercicio2_2()
        print("-" * 60)
        ejercicio3()
        print("-" * 60)
        ejercicio4()


if __name__ == "__main__":
    # Permite ejecutar con argumentos opcionales
    if len(sys.argv) > 1:
        try:
            main(int(sys.argv[1]))
        except ValueError:
            print("[Error] El número de ejercicio es entre 1 y 4.")
            sys.exit(1)
    else:
        main()
