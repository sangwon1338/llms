from vllm import HuggingFaceLLM
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.chains import RAGChain
import streamlit as st

# vLLM 실행 예제 - 간단한 실행
def vllm_basic_example():
    model_name = "meta-llama/Llama-3.2-1B"
    llm = HuggingFaceLLM(model_name=model_name)

    query = "vLLM을 사용한 모델의 장점은 무엇인가요?"
    result = llm.generate(query)
    print("vLLM 응답:", result)

# Streamlit 기반 vLLM 챗봇
def vllm_chatbot():
    llm = HuggingFaceLLM(model_name="meta-llama/Llama-3.2-1B")

    st.title("vLLM 기반 Chatbot")
    user_input = st.text_input("질문을 입력하세요:")

    if user_input:
        response = llm.generate(user_input)
        st.write("챗봇 응답:", response)

# RAG 파이프라인 구성
def vllm_rag_pipeline():
    embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

    data = [
        "vLLM은 빠르고 최적화된 언어 모델 실행을 지원합니다.", 
        "RAG는 검색을 통해 관련 정보를 기반으로 답변을 생성합니다.", 
        "vLLM은 실시간 상호작용이 필요한 환경에서 유용합니다."
    ]

    embeddings = [embedding_model.encode(doc) for doc in data]
    vector_store = FAISS.from_embeddings(embeddings, data)

    llm = HuggingFaceLLM(model_name="meta-llama/Llama-3.2-1B")
    rag_chain = RAGChain(llm=llm, retriever=vector_store.as_retriever())

    query = "vLLM의 장점은 무엇인가요?"
    result = rag_chain.run(query)
    print("vLLM RAG 응답:", result)

if __name__ == "__main__":
    print("1. vLLM 기본 실행")
    vllm_basic_example()

    print("2. RAG 파이프라인 실행")
    vllm_rag_pipeline()
