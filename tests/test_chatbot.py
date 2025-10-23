import os
import pytest
from pathlib import Path
from src.chatbot import ChatBot
from src.vector_database import VectorDDBB

MD_PATH = Path(os.getenv("TEST_DOC", Path(__file__).resolve().parents[1] / "data" / "ai-engineer-evaluation-test.md"))

QUESTIONS = [
    "¿Cuál es la pregunta que se debe responder en el ejercicio 1: Tu primera conexión IA?",
    "¿Cuáles son los Bonus Points generales que engloban todo el proceso?",
    "¿Qué modelos hay disponibles para el uso en el ejercicio?",
]

@pytest.fixture(scope="session")
def chatbot():
    if not MD_PATH.exists():
        pytest.skip(f"No se encontró el documento en {MD_PATH}. "
                    f"Colócalo ahí o usa TEST_DOC=/ruta/alternativa.md")
    db = VectorDDBB()
    db.load_document_from_path(MD_PATH)
    return ChatBot(db)

@pytest.mark.parametrize("q", QUESTIONS)
def test_example_questions_return_nonempty(chatbot, q):
    """El chatbot debe devolver contenido no vacío para cada pregunta de ejemplo."""
    ans = chatbot.answer_question(q)
    assert isinstance(ans, str)
    assert ans.strip() != ""
    # Asegura que no devuelva un mensaje de fallback genérico
    assert "no he encontrado" not in ans.lower()
    assert "no encontrado" not in ans.lower()
