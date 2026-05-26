# Helicone

LLM 옵저버빌리티에 1차 초점을 둔 게이트웨이. OpenAI SDK 의 `baseURL` 만 Helicone proxy 로 바꾸면 호출별 로깅·비용·지연 추적이 자동으로 활성화된다.

> ⚠️ **2026.03.03 Mintlify 가 Helicone 을 인수, 이후 maintenance mode 전환**. 보안 패치 / 신규 모델 추가 / 버그 픽스 / 성능 픽스는 계속 배포되나, **신규 기능 개발은 중단** 발표. 신규 도입 시 이 상태를 반드시 고려할 것 — 단기 사용·OSS 셀프호스팅으로는 여전히 유효한 선택지지만, 장기 기능 로드맵에 의존하는 결정은 권장하지 않음.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0). 메인 [`Helicone/helicone`](https://github.com/Helicone/helicone) + 별도 [`Helicone/ai-gateway`](https://github.com/Helicone/ai-gateway) (Rust 기반 고성능 게이트웨이) 모두 Apache 2.0.
- **비용**:
  - 셀프호스팅: **무료**.
  - Helicone Cloud (us.helicone.ai): **부분 무료** — 무료 티어 월 10k 요청, 이후 종량제·플랜제.

## 강점

- OpenAI SDK 의 `baseURL` 만 바꿔도 동작 → 통합 비용 거의 0.
- 로그·비용·지연·세션·사용자 단위 대시보드.
- async logging SDK(OpenLLMetry 기반)로 proxy 우회 후 비동기 로깅도 가능.

## 사용 방식

| 모드 | 형태 | 비고 |
|---|---|---|
| **Proxy** (권장) | OpenAI SDK 의 `base_url` 을 `https://oai.helicone.ai/v1` 으로 변경, `Helicone-Auth` 헤더 주입 | 통합 5분 |
| **Async logging SDK** | proxy 안 거치고 호출, 별도 SDK 가 비동기로 로그 push | 지연 최소화가 중요할 때 |
| **Self-hosted Gateway (Rust)** | `ai-gateway` 리포지토리의 OSS 게이트웨이 자체 운영 | 폐쇄망/엔터프라이즈 |

본 폴더 예제는 **Proxy 모드** (가장 흔한 사용 방식) 입니다.

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
# Python
python chat.py

# TypeScript
npm run chat
```

## 참고 링크

- 공식 문서: https://docs.helicone.ai
- GitHub (메인): https://github.com/Helicone/helicone
- GitHub (Rust 게이트웨이): https://github.com/Helicone/ai-gateway
- Async logging: https://docs.helicone.ai/getting-started/integration-method/async
- 셀프호스팅: https://docs.helicone.ai/getting-started/self-host/overview
