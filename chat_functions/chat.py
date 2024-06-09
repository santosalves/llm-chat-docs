from json import load as load_config


def carregar_configuracoes():
    try:
        with open('conf/app_config.json', 'r') as config_file:
            config = load_config(config_file)

    except FileNotFoundError:
        print('''
              Arquivo de configuração não encontrado, crie um arquivo chamado 'config.json' 
              na pasta 'conf' do projeto com as configuraçes.
              ''')

    return config


def entrada_do_usuario(input_client='CLI'):
    if input_client == 'CLI':
        return str(input('\033[32m' + '>>> ' + '\033[m'))
    elif input_client == 'WEB':
        from streamlit import chat_input, chat_message, write

        user_input = chat_input("Digite sua mensagem...")

        if user_input:
            with chat_message('user'):
                write(user_input)

            return user_input


def resposta_llm(llm_connection, pergunta):
    return llm_connection.invoke(pergunta)


def resposta_llm_stream(llm_connection, pergunta):
    for token in llm_connection.stream(pergunta):
        print(token, end='')

    return ''


def tente_novamente():
    print('Entrada inválida, digite algo coerente!')


def ajuda():
    comandos = '''
        Comandos:
        /help - Mostra essa mensagem
        /sair - Encerra o programa
    '''
    
    print(comandos)
