from langchain.docstore.document import Document

# 샘플 문서 추가
documents = [
    Document(page_content="1708년 강희제는 황태자 윤잉이 주색잡기에 빠져있고 패륜을 저질렀다고 하여 황태자에서 폐위시켰습니다."),
    Document(page_content="1911년 보호된 이후 남방해달 서식지는 확장되었지만 최근 해달이 조개를 통해 독소에 감염되어 위험이 증가하고 있습니다."),
    Document(page_content="한국 전쟁 당시 장진호 전투는 혹독한 겨울 날씨 속에서 벌어졌으며, 영하 37도까지 내려간 기온이 전투를 더욱 어렵게 만들었습니다.")
]

vectorstore.add_documents(documents)
