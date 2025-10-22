from src.vector_database import VectorDDBB

class ChatBot:
    def __init__(self, vector_db: VectorDDBB):
        self.vector_db = vector_db
        self.llm = vector_db.llm

    def _system_prompt(self) -> str:
        return "Eres un asistente conciso que responde SOLO usando el contexto proporcionado. Si la respuesta no está en el contexto, responde: 'No aparece en el documento'. Cita el título o la sección si es claro en el texto del chunk."
    
    def _construct_user_prompt(self, question: str, context: str) -> str:
        return f"""CONTEXTO (extractos de la guía):
                   {context}
                   ---
                   PREGUNTA:
                   {question}
                   ---
                   INSTRUCCIÓN:
                   Responde basándote únicamente en el contexto."""

    def answer_question(self, question: str) -> str:
        nearest_chunks = self.vector_db.nearest_chunks(question)
        context = "\n".join(nearest_chunks)
        user_prompt = self._construct_user_prompt(question, context)
        response = self.llm.call(self._system_prompt(), user_prompt)
        return response
