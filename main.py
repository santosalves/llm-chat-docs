from os import system
from langchain_community.llms import Ollama
from chat_functions import chat, ram_rag


def main():
    system("clear")

    try:
        llm = Ollama(**chat.carregar_configuracoes())
    except:
        print("Não foi possível carregar as configuraçes do LLM. Verifique o arquivo de configurações!")

    vectordb = ram_rag.carregar_docs()

    while True:
        prompt = chat.entrada_do_usuario()
        query = vectordb.similarity_search(prompt)

        match prompt.strip():
            case "/sair":
                break
            case "/help" | "/?":
                chat.ajuda()
            case "":
                chat.tente_novamente()
            case _:
                print(chat.resposta_llm(llm, prompt + query[0].page_content))


if __name__ == "__main__":
    main()
