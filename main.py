from os import system
from langchain_community.llms import Ollama
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from chat_functions import chat, ram_rag
from time import sleep
from dotenv import load_dotenv
from os import getenv


def app():
    system('clear')
    load_dotenv()
    set_llm_cache(InMemoryCache())

    try:
        llm = Ollama(**chat.carregar_configuracoes())
    except:
        print('Não foi possível carregar as configurações do LLM. Verifique o arquivo de configurações!')

    vectordb = ram_rag.carregar_docs(getenv('DOCUMENTO'))

    while True:
        prompt = chat.entrada_do_usuario()
        try:
            query = vectordb.invoke(prompt)
            query = query[0].page_content
        except Exception as e:
            print(f'Erro ao invocar o vetor DB: {e}')
            continue

        match prompt.strip():
            case '/sair':
                break
            case '/help' | '/?':
                chat.ajuda()
            case '':
                chat.tente_novamente()
            case _:
                for _ in range(3):
                    try:
                        print(chat.resposta_llm_stream(llm, prompt + query))
                        break
                    except Exception as e:
                        e = str(e).split('.')[0].replace('Details', '').strip()
                        print(f'Erro ao chamar Ollama: \033[91m{e}\033[m\n')
                        sleep(5)
                else:
                    print('Falha ao obter resposta do Ollama após várias tentativas.')


if __name__ == '__main__':
    app()
