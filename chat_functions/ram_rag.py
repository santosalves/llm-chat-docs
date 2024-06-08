def carregar_docs():
    from langchain_community.document_loaders import TextLoader
    from langchain_community.vectorstores import FAISS
    from langchain_text_splitters import CharacterTextSplitter
    from langchain_community import OllamaEmbeddings
    from json import load as load_config

    carregar_doc = TextLoader("./docs/*")
    documentos = carregar_doc.load()

    fragmenta_texto = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = fragmenta_texto.split_documents(documentos)

    embeddings = OllamaEmbeddings(**load_config("../conf/rag_confs.json"))
    db = FAISS.from_documents(docs, embeddings)

    print(db.index.ntotal)

