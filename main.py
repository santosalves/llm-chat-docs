from langchain_community.llms import Ollama
from os import system
from json import load as load_config


def resposta_llm(llm_connection, pergunta):
    for token in llm_connection.stream(pergunta):
        print(token, end="")

    return ""


def entrada_do_usuario():
    return str(input(">>> "))


def tente_novamente():
    print("Entrada inválida, digite algo coerente!")


def ajuda():
    comandos = """
    Comandos:
        /help - Mostra essa mensagem
        /sair - Encerra o programa
    """
    print(comandos)


def main():
    system("clear")

    with open('config.json', 'r') as config_file:
        conf = load_config(config_file)
    config_file.close()

    llm = Ollama(**conf)

    while True:
        prompt = entrada_do_usuario()
        match prompt:
            case "/sair":
                break
            case "/help":
                ajuda()
            case "/?":
                ajuda()
            case "":
                tente_novamente()
            case " ":
                tente_novamente()
            case _:
                print(resposta_llm(llm, prompt))


if __name__ == "__main__":
    main()
