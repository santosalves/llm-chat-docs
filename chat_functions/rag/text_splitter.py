from langchain_text_splitters import CharacterTextSplitter


class TextSplitter:
    def __init__(self, chunk_size, chunk_overlap):
        self._chunk_size = str(chunk_size)
        self._chunk_overlap = str(chunk_overlap)


    def split_docs(self, documents):
        return CharacterTextSplitter(self._chunk_size, self._chunk_overlap).split_documents(documents)
