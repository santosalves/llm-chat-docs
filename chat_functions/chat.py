def carregar_configuracoes():
    from json import load as load_config


    try:
        with open("../conf/app_config.json", "r") as config_file:
            config = load_config(config_file)

    except FileNotFoundError:
        print("""
              Arquivo de configuração não encontrado, crie um arquivo chamado 'config.json' 
              na pasta 'conf' do projeto com as configuraçes.
              """)

    return config


def resposta_llm(llm_connection, pergunta):
    return llm_connection.invoke(pergunta)


def resposta_llm_stream(llm_connection, pergunta):
    for token in llm_connection.stream(pergunta):
        print(token, end="")

    return ""


def entrada_do_usuario():
    return str(input("\033[32m" + ">>> " + "\033[m"))


def tente_novamente():
    print("Entrada inválida, digite algo coerente!")


def ajuda():
    comandos = """
    Comandos:
        /help - Mostra essa mensagem
        /sair - Encerra o programa
    """
    print(comandos)
