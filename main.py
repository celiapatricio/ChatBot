from src.llm import LLM

def main():
    llm = LLM()
    response = llm.call("How many 'a' are in the word 'MasOrange'?")
    print(response)

if __name__ == "__main__":
    main()