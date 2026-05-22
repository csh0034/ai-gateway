# LiteLLM

100+ LLM provider 를 단일 OpenAI 호환 인터페이스로 호출하는 OSS 게이트웨이.

## 강점

- Python 네이티브 SDK로 `litellm.completion(...)` 한 줄에 OpenAI / Anthropic / Bedrock / Vertex 등 호출.
- 동일 인터페이스에서 fallback, 재시도, 비용 추적, 가드레일 내장.
- `litellm --model ...` 으로 OpenAI 호환 proxy 서버를 띄울 수도 있음 (이 모드에서는 모든 언어가 OpenAI SDK로 접근 가능).

## TypeScript 지원

LiteLLM은 **Python 네이티브 SDK만** 제공합니다. TS에서 LiteLLM의 라우팅/통합을 쓰려면 LiteLLM proxy 서버를 띄우고 OpenAI Node SDK 의 `baseURL` 을 그 서버로 가리키는 방식이어야 하므로, 이 폴더에는 Python 예제만 둡니다.

## 설치 & 환경변수

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # 후 키 채우기
```

`.env.example` 의 키 중 사용할 모델의 키만 채우면 됩니다.

## 실행

```bash
python chat.py
```

## 참고 링크

- 공식 문서: https://docs.litellm.ai
- GitHub: https://github.com/BerriAI/litellm
- Proxy 모드: https://docs.litellm.ai/docs/proxy/quick_start
