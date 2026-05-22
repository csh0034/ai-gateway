# OpenRouter

단일 키로 수백 개 모델(OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek 등)에 접근하는 호스팅 게이트웨이.

## 강점

- **셋업이 가장 빠름**: 회원가입 → 키 발급 → `baseURL` 변경 한 줄로 끝.
- 자동 fallback, 모델별 가격/지연 비교, 무료 모델도 다수 제공.
- 비용 모델: 토큰 사용량 기준 + 약 5% 마크업.

## 작동 방식

OpenAI 호환 API 를 노출하므로, 기존 OpenAI SDK 의 `baseURL` 만 `https://openrouter.ai/api/v1` 로 바꾸면 됩니다.

모델명은 `provider/model` 형식 (예: `anthropic/claude-haiku-4-5`, `openai/gpt-4o-mini`).

## 설치 & 환경변수

### Python

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### TypeScript

```bash
cd typescript
npm install
cp .env.example .env
```

## 실행

- Python: `python chat.py`
- TypeScript: `npm start`

## 참고 링크

- 공식 문서: https://openrouter.ai/docs
- 모델 목록/가격: https://openrouter.ai/models
- Quickstart: https://openrouter.ai/docs/quickstart
