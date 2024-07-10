from os import getenv


def entrada_do_usuario():
    print(f'\033[93mDocumento de contexto: {getenv("DOCUMENTO")}\033[0m')

    return str(input('\033[32m' + '>>> ' + '\033[m'))


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
