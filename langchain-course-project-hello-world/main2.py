from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
#from langchain_ollama import ChatOllama # es de Facebook
#en una variable de entorno del sistems debo tener la OPENAI_API_KEY=
load_dotenv()


def main():
    print("Hello from langchain-course!")

if __name__ == "__main__":
    main()
