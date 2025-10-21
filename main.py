from src.llm import LLM


def main():
    llm = LLM()
    
    # Ejercicio 1: conexión básica con OpenAI
    response1 = llm.call("How many 'a' are in the word 'MasOrange'?")
    print(response1)

    # Ejercicio 2: conexión básica con embedding
    vec2 = llm.get_embedding("You shall not pass!")
    print(vec2)
    print(f"Embedding length: {len(vec2)}")

if __name__ == "__main__":
    main()