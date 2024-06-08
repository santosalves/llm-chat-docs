from os import system
from langchain_community.llms import Ollama
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from chat_functions import chat, ram_rag


def main():
    system("clear")
    set_llm_cache(InMemoryCache())

    try:
        llm = Ollama(**chat.carregar_configuracoes())
    except:
        print("Não foi possível carregar as configuraçes do LLM. Verifique o arquivo de configurações!")

    vectordb = ram_rag.carregar_docs()

    while True:
        prompt = chat.entrada_do_usuario()
        query = vectordb.invoke(prompt)
        query = query[0].page_content

        match prompt.strip():
            case "/sair":
                break
            case "/help" | "/?":
                chat.ajuda()
            case "":
                chat.tente_novamente()
            case _:
                print(chat.resposta_llm_stream(llm, prompt + query))


if __name__ == "__main__":
    main()

# Qual é o veículo vendido e quantos KM ele possui? Responda no formato: O veiculo {veiculo} possui {km} KMs