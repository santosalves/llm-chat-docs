from chat_functions.rag.document_loader import DocumentLoader
from chat_functions.rag.text_splitter import TextSplitter
from chat_functions.rag.vectordb import VectorDb
from chat_functions.rag.embeddings import Embeddings
from chat_functions.config_reader import ConfigReader
from os import getenv


class RamRag:
    def __init__(self, provider):
        self._config = ConfigReader('conf/rag_config.json')
        self._provider = Embeddings(**self._config.get_config())

        if provider == 'ollama':
            self._embeddings = self._provider.ollama()


    def process_doc(self, doc_name):
        print('\033[92mLendo o DB local...\033[0m')
        load_doc = DocumentLoader(f'docs/{doc_name}', f'{doc_name.split(".")[-1]}')
        doc = load_doc.load()

        shard_text = TextSplitter(getenv('CHUNK_SIZE'), getenv('CHUNK_OVERLAP'))
        shard_doc = shard_text.split_docs(doc)

        db = VectorDb(f'data/db_{doc_name.split(".")[0]}', self._embeddings, shard_doc)
        return db.faiss_retriever()
