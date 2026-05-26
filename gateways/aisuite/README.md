# aisuite

Andrew Ng 팀이 공개한 매우 가벼운 통합 SDK. `provider:model` 한 문자열만 바꾸면 OpenAI / Anthropic / AWS / Azure / Cerebras / Groq / HuggingFace / Mistral / Ollama / Sambanova / Watsonx 등으로 전환된다.

## 라이선스 / 비용

- **라이선스**: OSS (MIT).
- **비용**: 무료 (각 provider 사용료는 별도).
- **TypeScript 지원**: ❌ Python only. 본 폴더는 Python 예제만 둡니다.

## 강점

- 의존성 최소 — `pip install aisuite` 한 줄.
- 거의 OpenAI SDK 와 동일한 호출 인터페이스 (`client.chat.completions.create`).
- multi-turn agentic loop (`max_turns`), Python 함수를 그대로 tool 로 전달 가능.

## 한계

- 라우팅·폴백·비용 추적 같은 운영 기능은 거의 없음 — 그쪽 요구가 있다면 LiteLLM / Portkey 권장.
- 활성 개발 속도는 LiteLLM 대비 느린 편 (학습·프로토타입에 적합).

## 설치 & 환경변수

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

## 실행

```bash
python chat.py
```

## 참고 링크

- GitHub: https://github.com/andrewyng/aisuite
- 발표 (Andrew Ng X): https://x.com/AndrewYNg/status/1861085482526105842
- 지원 provider 목록: https://github.com/andrewyng/aisuite#supported-providers
