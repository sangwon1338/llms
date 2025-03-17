from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma

# Chroma DB 설정
persist_directory = "./chroma_db"
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-large-instruct",
    model_kwargs={"device": "cuda"},
    encode_kwargs={"normalize_embeddings": True}
)

vectorstore = Chroma(persist_directory=persist_directory, embedding_function=embeddings)
