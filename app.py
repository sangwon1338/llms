import streamlit as st
from langchain.vectorstores import Chroma

# Chroma 벡터 데이터베이스 로드
persist_directory = "./chroma_db"
vectorstore = Chroma(persist_directory=persist_directory)

from generate_response import generate_response

st.title("EEVE-Korean Chatbot")
st.write("한국사, 생물학, 전쟁사 등의 지식을 기반으로 질문에 답변하는 챗봇입니다.")

user_input = st.text_input("질문을 입력하세요:")

if st.button("답변 받기"):
    if user_input:
        retriever = vectorstore.as_retriever()
        relevant_docs = retriever.get_relevant_documents(user_input)
        context = "\n".join([doc.page_content for doc in relevant_docs])

        with st.spinner("답변을 생성 중입니다..."):
            generated_response = generate_response(context, user_input)

        st.write(f"**챗봇:** {generated_response}")
    else:
        st.warning("질문을 입력하세요.")
