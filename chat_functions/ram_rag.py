def carregar_docs(nome_do_doc):
    from chat_functions.rag.document_loader import DocumentLoader
    from chat_functions.rag.text_splitter import TextSplitter
    from langchain_community.vectorstores import FAISS
    from chat_functions.rag.embeddings import Embeddings
    from chat_functions.config_reader import ConfigReader
    from os import system, getenv
    from time import sleep


    print('\033[92mLendo o DB local...\033[0m')
    carregar_doc = DocumentLoader(f'docs/{nome_do_doc}', f'{nome_do_doc.split(".")[-1]}')
    documentos = carregar_doc.load()

    fragmenta_texto = TextSplitter(getenv('CHUNK_SIZE'), getenv('CHUNK_OVERLAP'))
    docs = fragmenta_texto.split_docs(documentos)

    config = ConfigReader('conf/rag_config.json')
    provider = Embeddings(**config.get_config())
    embeddings = provider.ollama()
    
    while True:
        try:
            db = FAISS.load_local(f'data/db_{nome_do_doc.split(".")[0]}', embeddings, allow_dangerous_deserialization=True)
            break
        except RuntimeError:
            print('\033[31mNão encontrado! Gerando um novo DB local...\033[0m')
            
            db = FAISS.from_documents(docs, embeddings)
            db.save_local(f'data/db_{nome_do_doc.split(".")[0]}')

            sleep(4)
            system('clear')

    return db.as_retriever()
