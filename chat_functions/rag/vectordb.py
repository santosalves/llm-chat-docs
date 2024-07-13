from time import sleep
from os import system


class VectorDb:
    def __init__(self, file_path, embeddings, docs):
        self._file_path = file_path
        self._embeddings = embeddings
        self._docs = docs


    def faiss_retriever(self):
        from langchain_community.vectorstores import FAISS


        while True:
            try:
                db = FAISS.load_local(self._file_path, self._embeddings, allow_dangerous_deserialization=True)
                break
            except RuntimeError:
                print('\033[31mNão encontrado! Gerando um novo DB local...\033[0m')
                
                db = FAISS.from_documents(self._docs, self._embeddings)
                db.save_local(self._file_path)
                
                sleep(4)
                system('clear')
            
        return db.as_retriever()
