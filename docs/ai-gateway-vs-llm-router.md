# AI Gateway vs LLM Router

자주 혼용되지만 책임 레이어가 다르다. 실제 시스템에서는 두 레이어를 함께 쓰는 경우가 많다.

## 한 줄 요약

- **Proxy**: 요청을 그대로 전달하는 운송 레이어.
- **Router**: 어떤 모델/제공자에게 보낼지 결정하는 의사결정 레이어.
- **Gateway**: 인증/요금/속도제한/감사/가드레일 등 정책을 적용하는 정책 레이어.

대부분의 상용 플랫폼은 셋을 합쳐 "통합 API + 라우팅 + 정책"으로 제공한다.

## 책임 비교

| 항목 | AI Gateway | LLM Router |
|---|---|---|
| 1차 목적 | 통합 API, 정책 적용 | 적합한 모델 선택 |
| 다루는 입력 | 모든 요청 | 모든 요청 (라우팅 판단 필요) |
| 결정 기준 | 정책(예산, 권한, 한도) | 프롬프트 특성(난이도, 도메인, 비용/품질) |
| 일반 기능 | 인증, 요금 추적, fallback, 로깅, 가드레일 | 모델 분류, 강·약모델 페어, threshold 학습 |
| 대표 서비스 | LiteLLM, Portkey, Helicone, OpenRouter, Kong AI Gateway | RouteLLM, NVIDIA LLM Router, NotDiamond(상용) |

## 어떻게 함께 쓰는가

```
Application
    │
    ▼
[ AI Gateway ]  ←  인증/요금/로깅/가드레일
    │
    ▼
[ LLM Router ]  ←  프롬프트 분류 → 모델 선택
    │
    ├──▶ GPT-4 / Claude Opus  (어려운 질문, 코드 생성)
    └──▶ GPT-4o-mini / Haiku  (간단 분류, 요약)
```

- 게이트웨이는 어떤 모델이 호출되든 동일한 정책을 강제.
- 라우터는 게이트웨이 안쪽에서 실제 모델 선택을 담당.
- LiteLLM/Portkey 같은 일부 게이트웨이는 단순 fallback 수준의 라우팅을 내장 — 본격 모델 선택 라우팅이 필요하면 RouteLLM 같은 전용 라우터 결합.

## 선택 기준

| 상황 | 추천 |
|---|---|
| 빠른 프로토타입, 다수 provider 통합 호출 | LiteLLM (Python) 또는 OpenRouter |
| 본격 운영: 가드레일/감사/팀별 권한 | Portkey |
| 옵저버빌리티 우선 (비용/지연 추적) | Helicone |
| 비용 최적화: 어려운 질의만 강모델로 | RouteLLM (Gateway 안쪽에서) |

## 주의점

- Gateway 단의 fallback과 Router는 다른 문제다. fallback은 "장애 시 다른 모델", Router는 "처음부터 다른 모델".
- 학습형 Router(예: RouteLLM)는 학습된 도메인 밖에서 성능이 떨어질 수 있음 — 도메인 평가셋으로 임계값을 재튜닝 필요.
- Gateway에 캐시를 켤 때 동일 프롬프트로 다른 사용자가 캐시된 응답을 받는 보안/프라이버시 이슈 점검.
