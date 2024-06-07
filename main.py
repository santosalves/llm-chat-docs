from os import system
from langchain_community.llms import Ollama
from chat_functions import chat


def main():
    system("clear")

    llm = Ollama(**chat.carregar_configuracoes())

    while True:
        prompt = chat.entrada_do_usuario()

        match prompt.strip():
            case "/sair":
                break
            case "/help" | "/?":
                chat.ajuda()
            case "":
                chat.tente_novamente()
            case _:
                print(chat.resposta_llm(llm, prompt))


if __name__ == "__main__":
    main()
