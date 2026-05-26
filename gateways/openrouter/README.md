# OpenRouter

400+ 모델을 단일 키·OpenAI 호환 endpoint 로 호출하는 호스팅 SaaS. `openrouter/auto` 같은 메타 모델을 쓰면 OpenRouter 가 자동으로 라우팅까지 수행.

## 라이선스 / 비용

- **라이선스**: **Proprietary (백엔드 closed source)**. 공식 클라이언트 SDK (`@openrouter/sdk` TS, Python) 는 공개되지만 라우팅·정산 백엔드 비공개.
- **비용**: **부분 무료**.
  - **크레딧 모드**: 크레딧 충전 → 호출 시 자체 마진 포함 청구.
  - **BYOK (Bring Your Own Key)**: 사용자 본인 provider 키 등록 → 월 1M 요청까지 무료, 초과분 5% 수수료 (향후 고정 월 구독 전환 예정).
  - 무료 카탈로그 모델(`*:free`) 도 일부 존재.
- **폐쇄망**: ❌ 호스팅 전용, 자체 호스팅 불가.

## 강점

- OpenAI SDK 의 `baseURL` 만 바꿔 즉시 사용 — 통합 비용 거의 0.
- 400+ 모델 (OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, xAI 등).
- `openrouter/auto` 모델로 라우터를 OpenRouter 측에 맡길 수 있음 (NotDiamond 기반).

## 사용 방식

| 모드 | 형태 | 비고 |
|---|---|---|
| **Credit** | OpenRouter 가 사용자 카드로 청구 + 마진 | 가장 빠른 시작 |
| **BYOK** | provider 키 본인 등록 → 월 1M 무료, 초과분 5% | 비용 통제 우선 |
| **Auto router** | model 을 `openrouter/auto` 로 지정 | OpenRouter 가 프롬프트 분석 후 자동 선택 |

본 폴더 예제는 **OpenAI SDK + baseURL 변경** 방식입니다 (크레딧/BYOK 모두 동일 코드).

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

```bash
python chat.py        # Python
npm run chat          # TypeScript
```

## 참고 링크

- 공식: https://openrouter.ai
- 문서: https://openrouter.ai/docs
- 모델 카탈로그: https://openrouter.ai/models
- BYOK 가이드: https://openrouter.ai/docs/use-cases/byok
- Auto Router: https://openrouter.ai/openrouter/auto
