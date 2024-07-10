def carregar_docs(nome_do_doc):
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS
    from langchain_text_splitters import CharacterTextSplitter
    from langchain_community.embeddings import OllamaEmbeddings
    from chat_functions.config_reader import ConfigReader
    from os import system
    from time import sleep


    config = ConfigReader('conf/rag_config.json')

    print('\033[92mLendo o DB local...\033[0m')
    carregar_doc = PyPDFLoader(f'docs/{nome_do_doc}')
    documentos = carregar_doc.load_and_split()

    fragmenta_texto = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = fragmenta_texto.split_documents(documentos)

    embeddings = OllamaEmbeddings(**config.get_config())
    
    while True:
        try:
            db = FAISS.load_local(f'data/db_{nome_do_doc[:-4]}', embeddings, allow_dangerous_deserialization=True)
            break
        except RuntimeError:
            print('\033[31mNão encontrado! Gerando um novo DB local...\033[0m')
            
            db = FAISS.from_documents(docs, embeddings)
            db.save_local(f'data/db_{nome_do_doc[:-4]}')

            sleep(4)
            system('clear')

    return db.as_retriever()
