# 서비스 한눈에 보기 (Services Overview)

채택 기준을 두지 않고 폭넓게 다루는 본 저장소의 모든 서비스를 **라이선스 / 비용 / 카테고리 / 코드 예제 유무** 한 페이지로 정리.

## Gateway 카테고리

| 서비스 | 라이선스 | 비용 | 모드 | Py SDK | TS SDK | 코드 예제 |
|---|---|---|---|---|---|---|
| LiteLLM | OSS (MIT) · `enterprise/` 상용 | 무료 (Cloud 유료) | SDK + Proxy | ✅ | ❌ | ✅ Py |
| Portkey | OSS (Apache 2.0) | 무료 (호스팅 유료) | Gateway 서버 + SDK | ✅ | ✅ | ✅ Py + TS |
| Helicone | OSS (Apache 2.0) | 무료 (Cloud 부분 유료) | Proxy | (OpenAI SDK) | (OpenAI SDK) | ✅ Py + TS |
| OpenRouter | Proprietary | 부분 무료 (BYOK 1M/월) | SaaS (OpenAI 호환) | (OpenAI SDK) | (OpenAI SDK) | ✅ Py + TS |
| Cloudflare AI Gateway | Proprietary | 부분 무료 (Workers Free/Paid) | SaaS Proxy | (OpenAI SDK) | (OpenAI SDK) | ✅ Py + TS |
| aisuite | OSS (MIT) | 무료 | SDK | ✅ | ❌ | ✅ Py |
| Bifrost | OSS (Apache 2.0) | 무료 (매니지드 유료) | Go 게이트웨이 서버 | (OpenAI SDK) | (OpenAI SDK) | ❌ |
| Kong AI Gateway | OSS Apache 2.0 + 상용 Enterprise/Konnect | 부분 유료 | 게이트웨이 서버 | (OpenAI SDK) | (OpenAI SDK) | ❌ |
| AWS Bedrock | Proprietary | 종량제 유료 | AWS 서비스 | boto3 | AWS SDK JS | ❌ |
| Apache APISIX | OSS (Apache 2.0) | 무료 (API7 유료) | 게이트웨이 서버 | (OpenAI SDK) | (OpenAI SDK) | ❌ |
| Envoy AI Gateway | OSS (Apache 2.0) | 무료 | K8s 게이트웨이 | (OpenAI SDK) | (OpenAI SDK) | ❌ |
| MLflow AI Gateway | OSS (Apache 2.0) | 무료 | MLflow 서버 | mlflow.deployments | (OpenAI SDK) | ❌ |

## Router 카테고리

| 서비스 | 라이선스 | 비용 | 모드 | Py SDK | TS SDK | 코드 예제 |
|---|---|---|---|---|---|---|
| RouteLLM | OSS (Apache 2.0) | 무료 | Python Controller | ✅ | ❌ | ✅ Py |
| Martian | Proprietary | 부분 무료 (2,500 req free) | SaaS (OpenAI 호환) | (OpenAI SDK) | (OpenAI SDK) | ✅ Py + TS |
| Not Diamond | Proprietary | 부분 무료 (free tier + 유료) | 추천 API | ✅ | ✅ | ✅ Py + TS |
| vLLM Semantic Router | OSS (Apache 2.0) | 무료 | Envoy ExtProc | (OpenAI SDK) | (OpenAI SDK) | ❌ |
| NVIDIA LLM Router | OSS (MIT) + 모델 별도 라이선스 | 무료 (GPU/NIM 비용 별도) | NIM/Triton 서버 | (OpenAI SDK) | (OpenAI SDK) | ❌ |

> `(OpenAI SDK)` 는 별도 전용 SDK 없이 OpenAI SDK 의 `base_url` 을 게이트웨이로 가리켜 사용한다는 뜻입니다.

## "무료/유료" 표기 기준

- **무료**: 소스 / 바이너리 자체에 라이선스 비용 없음. (사용한 LLM provider 요금은 별도)
- **부분 무료**: 무료 티어 / BYOK / 일정량 무료 + 초과분 유료.
- **유료**: 기본 사용 자체에 비용 발생.

## 카테고리 노트

- **provider 통합형 (Gateway)**: LiteLLM, Portkey, aisuite, OpenRouter, Bifrost, MLflow AI Gateway — provider API 표준화.
- **옵저버빌리티 1차 (Gateway)**: Helicone, Cloudflare AI Gateway.
- **인프라 API Gateway 의 AI 확장**: Kong, Apache APISIX, Envoy AI Gateway.
- **단일 클라우드 매니지드 모델**: AWS Bedrock.
- **결정 레이어 (Router)**: RouteLLM, Martian, Not Diamond, vLLM Semantic Router, NVIDIA LLM Router.

같은 서비스가 여러 책임을 동시에 맡는 경우가 많아 분류는 1차 책임 기준입니다. 자세한 개념 비교는 [`ai-gateway-vs-llm-router.md`](./ai-gateway-vs-llm-router.md) 참고.

## 선택 가이드 (간단)

| 상황 | 추천 |
|---|---|
| Python 단일 앱, 빠르게 다수 provider 호출 | LiteLLM, aisuite |
| 운영 규모 (가상 키, 정책, UI) | Portkey, LiteLLM Proxy |
| 옵저버빌리티 최우선 | Helicone, Cloudflare AI Gateway |
| 기존 API Gateway 운영팀 | Kong AI Gateway, Apache APISIX |
| 단일 키로 다수 모델 카탈로그 | OpenRouter |
| K8s/Envoy 표준 라인 | Envoy AI Gateway (+ vLLM Semantic Router) |
| AWS 종속 + Bedrock 활용 | AWS Bedrock |
| 모델 선택 자동화 (학습형) | RouteLLM, Not Diamond, Martian |
| 폐쇄망 + 학습형 라우터 | RouteLLM, NVIDIA LLM Router, vLLM Semantic Router |
