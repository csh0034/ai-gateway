# Gateways

AI Gateway 서비스 사용 예제 모음. 카테고리·라이선스·비용을 한눈에 보고 폴더에서 상세 README 와 코드 예제(있는 경우)를 확인하세요.

`코드 예제 ✅` 는 SDK 임베드 또는 OpenAI 호환 endpoint 단순 호출만으로 동작하는 케이스입니다. `❌` 는 별도 게이트웨이 프로세스/K8s 등 인프라가 필요해 본 저장소는 README 만 둔 케이스입니다.

> **추천 순위 기준 (주관)**: 학습·일반 채택 관점에서 ① 도입 용이성(SDK 임베드 / OpenAI 호환) ② OSS 라이선스 자유도 ③ 커뮤니티 활성도·도입 사례 ④ 운영 상태(maintenance mode 등). 운영 요구사항이 다르면 순위가 뒤집힐 수 있습니다 (예: K8s 표준 라인 우선이면 Envoy AI Gateway 가 상위, AWS 종속 환경이면 Bedrock 상위).

| 추천 | 서비스 | 라이선스 | 비용 | 모드 | 코드 예제 | 한 줄 강점 |
|---|---|---|---|---|---|---|
| 1 | [litellm](./litellm/) | MIT (`enterprise/`는 상용) | 무료 | Python SDK + (선택) Proxy 서버 | ✅ | 100+ provider 통합 호출, SDK 임베드만으로 라우팅·폴백·비용 추적 |
| 2 | [portkey](./portkey/) | MIT (메인 LICENSE 기준, 2026.03 프로덕션 게이트웨이 OSS 머지) | 무료 (호스팅·엔터프라이즈는 유료) | Gateway 서버 + Py/TS SDK | ✅ | 1600+ 모델, 가드레일·옵저버빌리티 내장, edge 배포 가능 |
| 3 | [openrouter](./openrouter/) | Proprietary (백엔드 closed) | 부분 무료 (BYOK 월 1M req 무료) | OpenAI 호환 SaaS | ✅ | 400+ 모델 단일 키, openrouter/auto 자동 라우팅 |
| 4 | [cloudflare-ai-gateway](./cloudflare-ai-gateway/) | Proprietary | 부분 무료 (Workers Free/Paid) | 호스팅 프록시 (URL 재작성) | ✅ | Cloudflare edge 캐시·rate limit, 분석 대시보드 |
| 5 | [aisuite](./aisuite/) | MIT | 무료 | Python SDK 임베드 | ✅ | 매우 가벼운 통합 SDK, `provider:model` 한 줄 |
| 6 | [bifrost](./bifrost/) | Apache 2.0 | 무료 (매니지드는 유료) | 게이트웨이 서버 (Go, NPX/Docker) | ❌ | 초저지연(5K RPS 에서 ~11µs 오버헤드), 1000+ 모델 |
| 7 | [apisix-ai-gateway](./apisix-ai-gateway/) | Apache 2.0 (ASF 프로젝트) | 무료 (매니지드는 유료) | 게이트웨이 서버 (OpenResty 기반) | ❌ | ASF 정식 프로젝트, AI proxy/load balancing 플러그인 무료 |
| 8 | [kong-ai-gateway](./kong-ai-gateway/) | Apache 2.0 (OSS) + Enterprise/Konnect 상용 | 부분 유료 | 게이트웨이 서버 (Nginx 기반) | ❌ | 기존 Kong API Gateway 의 AI 확장, 엔터프라이즈 정책 |
| 9 | [envoy-ai-gateway](./envoy-ai-gateway/) | Apache 2.0 (CNCF) | 무료 | K8s 게이트웨이 (Envoy ExternalProcessor) | ❌ | CNCF 표준 라인, K8s 네이티브 |
| 10 | [mlflow-ai-gateway](./mlflow-ai-gateway/) | Apache 2.0 | 무료 | MLflow Python 서버 | ❌ | MLflow 트래킹 서버와 일체화, GenAI 거버넌스 |
| 11 | [helicone](./helicone/) | Apache 2.0 | 무료 (호스팅 SaaS 부분 유료) | Proxy (OpenAI SDK 의 baseURL 변경) | ✅ | 옵저버빌리티 1급, 1줄 통합 (⚠️ 2026.03 Mintlify 인수 후 maintenance mode) |
| 12 | [aws-bedrock](./aws-bedrock/) | Proprietary | 종량제 유료 | AWS SDK / Bedrock Runtime | ❌ | AWS 네이티브, IAM/VPC/PrivateLink, foundation model 마켓플레이스 |

## 카테고리 노트

- **provider 통합형**: LiteLLM, Portkey, aisuite, OpenRouter, Bifrost, MLflow AI Gateway — provider API 표준화가 1차 목적.
- **옵저버빌리티 중심**: Helicone, Cloudflare AI Gateway — 로깅/비용/지연 추적이 1차 목적.
- **인프라 API Gateway 의 AI 확장**: Kong AI Gateway, Apache APISIX, Envoy AI Gateway — 기존 API Gateway 스택에 AI 정책 추가.
- **클라우드 종속**: AWS Bedrock — 단일 클라우드 종속이지만 통합 환경에서는 강력.

분류는 1차 책임 기준이며 실제로는 여러 책임을 동시에 갖는 경우가 많습니다. 자세한 비교는 [`docs/ai-gateway-vs-llm-router.md`](../docs/ai-gateway-vs-llm-router.md) 참고.
