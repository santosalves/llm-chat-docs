class Embeddings:
    def __init__(self, **config):
        self._config = config
        print(self._config)


    def ollama(self):
        from langchain_community.embeddings import OllamaEmbeddings
        return OllamaEmbeddings(**self._config)

