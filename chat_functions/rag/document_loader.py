class DocumentLoader:
    def __init__(self, file_path, file_type):
        if file_type == 'pdf':
            from langchain_community.document_loaders import PyPDFLoader
            self.carregar_doc = PyPDFLoader(file_path).load_and_split()


    def load(self):
        return self.carregar_doc
