
# Converse sobre seus arquivos

## Intro

Este programa é uma aplicação de conversa inteligente que utiliza um Modelo de Linguagem Grande (LLM) para responder perguntas do usuário. Com base em um documento, o programa é capaz de entender e responder às consultas dos usuários, simulando uma conversa humana.

Com isso, você será capaz de responder dúvidas de forma rápida e simples sobre qualquer documento, como um contrato, livro, etc.

Todas as informações sobre o documento são carregadas na memória RAM, onde usamos como fonte de dados da VectorDB(FAISS).

## Requisitos

Para rodar este código, você precisará ter os seguintes pacotes e programas:

### Dependências

* Python 3.10 ou superior
* Instale os pacotes presentes no requirements.txt

### Arquivos/Paths de Configurações

* `.env`: Arquivo de configurações para variáveis de ambiente (opcional, mas recomendado).
* `conf/`: Contém os arquivos de configuraões para o uso do LLM,
para o modelo principal e outro exclusivo para RAG.
* `data/`: Contém os dados previamente exportados para consulta posterior, após o uso de um documento.
* `docs/`: Contém os documentos que serão lidos(individualmente) pelo programa.

### Variáveis Ambiente

* `DOCUMENTO`: Nome do arquivo a ser carregado no programa. O arquivo precisa estar dentro da pasta `docs/`.
* `CHUNK_SIZE`: Variável de ambiente que define o tamanho do chunk utilizado para fragmentar o texto.
* `CHUNK_OVERLAP`: Variável de ambiente que define o overlap entre chunks utilizado na fragmentação do texto.

## Como Executar

1. Clone ou baixe o repositório com o código fonte.
2. Instale as dependências Python usando o comando `pip install -r requirements.txt` (se você tiver um arquivo `requirements.txt`).
3. Configure as variáveis ambiente necessárias no arquivo `.env` (se você estiver utilizando).
4. Execute o código principal com o comando `python main.py`.

## Notas

* **Importante:** No momento, apenas o `provider` Ollama é aceito para RAG e CHAT.
* Para o uso com GPU, é necessário que o código seja executado a partir do Linux. Trocar a biblioteca `faiss-gpu` pela `faiss-cpu` permite execução em outros sistemas sem uso de placa de vídeo, porém com uma grande degradação da performance.
* O código pode precisar ser ajustado para funcionar corretamente em diferentes ambientes e sistemas.
