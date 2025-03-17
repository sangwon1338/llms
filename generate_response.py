import requests

def generate_response(context, query):
    full_prompt = f"당신은 저를 돕는 어시스턴트입니다. 반드시 한국어로 답해주세요.\n" \
                  f"다음 문서를 바탕으로 질문에 답하세요:\n\n{context}\n\n질문: {query}\n답변:"

    api_url = "http://localhost:8000/v1/completions"

    payload = {
        "model": "yanolja/EEVE-Korean-Instruct-10.8B-v1.0",
        "prompt": full_prompt,
        "max_tokens": 50,
        "temperature": 0.7,
        "top_p": 0.9
    }

    response = requests.post(api_url, json=payload)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return "오류 발생: LLM 서버에서 응답을 가져올 수 없습니다."
