# Cloudflare AI Gateway

Cloudflare 엣지 네트워크 위에 동작하는 호스팅 AI 프록시. 별도 인프라 없이 대시보드에서 게이트웨이를 만들고 URL 만 갈아 끼우면 캐싱·rate limit·로깅·분석이 동작.

## 라이선스 / 비용

- **라이선스**: **Proprietary** (Cloudflare 제품). OSS 아님.
- **비용**: **부분 무료**.
  - **Workers Free 플랜**: 게이트웨이 자체 무료, 월 100k 로그.
  - **Workers Paid ($5/월~)**: 월 1M 로그 + 추가 사용량 종량제.
  - **2026 신규**: 3rd-party 모델 사용량을 Cloudflare 인보이스로 통합 청구 옵션 (소액 거래 수수료).
- **폐쇄망**: ❌ Cloudflare 호스팅 전용, 자체 호스팅 불가.

## 강점

- 글로벌 엣지 캐시 → 동일 프롬프트 즉시 응답.
- 대시보드 분석·rate limit·필터·요청 재시도가 코드 변경 없이 동작.
- 100+ provider (OpenAI, Anthropic, AWS Bedrock, Google AI Studio, Groq, Replicate, Mistral, Cohere, HuggingFace, Workers AI 등) 통합.

## 사용 방식

OpenAI 호환 endpoint 가 제공되어 SDK 의 `baseURL` 만 다음과 같이 변경합니다:

```
https://gateway.ai.cloudflare.com/v1/{ACCOUNT_ID}/{GATEWAY_ID}/openai
```

다른 provider(Anthropic, AWS Bedrock 등)도 동일 URL 패턴에서 마지막 segment 만 `anthropic`, `aws-bedrock` 등으로 바꾸면 됩니다.

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

대시보드(https://dash.cloudflare.com/?to=/:account/ai/ai-gateway)에서 게이트웨이를 만든 후, 계정 ID 와 게이트웨이 이름을 환경변수에 채웁니다.

## 실행

```bash
python chat.py
npm run chat
```

## 참고 링크

- 공식: https://www.cloudflare.com/ai-gateway
- 문서: https://developers.cloudflare.com/ai-gateway
- 요금: https://developers.cloudflare.com/ai-gateway/reference/pricing
- Provider 별 사용법: https://developers.cloudflare.com/ai-gateway/usage/providers
- OpenAI 호환 endpoint: https://developers.cloudflare.com/ai-gateway/chat-completion
