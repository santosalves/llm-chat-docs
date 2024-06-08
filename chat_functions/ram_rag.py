def carregar_docs(nome_do_doc):
    from langchain_community.document_loaders import PyPDFLoader
    from langchain_community.vectorstores import FAISS
    from langchain_text_splitters import CharacterTextSplitter
    from langchain_community.embeddings import OllamaEmbeddings
    from json import load as load_config


    try:
        with open("../conf/rag_config.json", "r") as config_file:
            config = load_config(config_file)

    except FileNotFoundError:
        print("""
              Arquivo de configuração não encontrado, crie um arquivo chamado 'rag_config.json' 
              na pasta 'conf' do projeto com as configuraçes.
              """)

    carregar_doc = PyPDFLoader(f'../docs/{nome_do_doc}')
    documentos = carregar_doc.load_and_split()

    fragmenta_texto = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = fragmenta_texto.split_documents(documentos)

    embeddings = OllamaEmbeddings(**config)
    db = FAISS.from_documents(docs, embeddings)
    
    return db.as_retriever()
