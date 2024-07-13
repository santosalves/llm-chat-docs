def carregar_docs(nome_do_doc):
    from chat_functions.rag.document_loader import DocumentLoader
    from chat_functions.rag.text_splitter import TextSplitter
    from chat_functions.rag.vectordb import VectorDb
    from chat_functions.rag.embeddings import Embeddings
    from chat_functions.config_reader import ConfigReader
    from os import getenv


    print('\033[92mLendo o DB local...\033[0m')
    carregar_doc = DocumentLoader(f'docs/{nome_do_doc}', f'{nome_do_doc.split(".")[-1]}')
    documentos = carregar_doc.load()

    fragmenta_texto = TextSplitter(getenv('CHUNK_SIZE'), getenv('CHUNK_OVERLAP'))
    docs = fragmenta_texto.split_docs(documentos)

    config = ConfigReader('conf/rag_config.json')
    provider = Embeddings(**config.get_config())
    embeddings = provider.ollama()

    db = VectorDb(f'data/db_{nome_do_doc.split(".")[0]}', embeddings, docs)

    return db.faiss_retriever()
