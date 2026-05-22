# Helicone

OSS 옵저버빌리티 중심의 LLM 프록시. 로깅·비용·지연 추적이 1차 목적.

## 강점

- **1줄 통합**: 기존 OpenAI SDK 의 `baseURL` 만 Helicone proxy 로 바꾸고 `Helicone-Auth` 헤더 추가 → 자동 로깅.
- **Provider 무관**: OpenAI 외에 Anthropic 등도 각각의 proxy endpoint로 동일 패턴.
- 자체 호스팅 OSS + 호스팅 SaaS 모두 지원.

## 작동 방식

```
your app ─▶ Helicone proxy ─▶ provider(OpenAI/Anthropic)
            (로그/비용/지연 기록)
```

본 예제는 호스팅 endpoint (`https://oai.helicone.ai/v1`) 기준입니다.

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

- 공식 문서: https://docs.helicone.ai
- GitHub: https://github.com/Helicone/helicone
- Proxy 통합 가이드: https://docs.helicone.ai/getting-started/integration-method/openai-proxy
