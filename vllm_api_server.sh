# vLLM API 서버 실행 명령어
python -m vllm.entrypoints.api_server \
    --model yanolja/EEVE-Korean-Instruct-10.8B-v1.0 \
    --quantization gptq \
    --dtype auto \
    --host 0.0.0.0 --port 8000
