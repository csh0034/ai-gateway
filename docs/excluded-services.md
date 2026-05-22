# 제외된 서비스

이 저장소는 **"SDK 만으로 내 앱에 임베드해서 직접 게이트웨이/라우터를 개발할 수 있는"** 무료 OSS 서비스만 다룹니다. 이 기준에 안 맞는 서비스는 아래와 같이 제외되었습니다.

## 채택 기준 (재확인)

1. 무료 (OSS 또는 무료 사용량 호스팅)
2. **별도 게이트웨이 프로세스 없이 SDK 라이브러리만으로 내 앱에 임베드 가능**
   - SDK가 provider API 한테 직접 HTTP 호출.
   - 게이트웨이/프록시 전용 백엔드 서버를 추가로 띄울 필요가 없어야 함.
3. 폐쇄망에서도 사용 가능 (자체 호스팅 LLM 백엔드만 연결하면 즉시 동작)

## 채택된 서비스

| 카테고리 | 서비스 | 언어 |
|---|---|---|
| Gateway | LiteLLM | Python only |
| Router | RouteLLM | Python only |

## 제외된 서비스

### Portkey — 제외

- **사유**: SDK는 단순 클라이언트이고, 실제 동작에는 **Portkey gateway 프로세스(호스팅 `api.portkey.ai` 또는 자체 호스팅 Docker)가 별도로 떠 있어야 함**. SDK 임베드만으로 완결되지 않음.
- **통신 경로**: `내 앱 + SDK ──HTTP──▶ Portkey gateway ──HTTP──▶ provider`
- **OSS 여부**: 2026-03-24 Apache 2.0 전환 발표(Gateway 2.0 정식 OSS화), 단 main 브랜치 LICENSE 파일은 작성 시점 기준 여전히 MIT로 표기 — 자체 호스팅은 가능하지만 운영 부담 추가.
- **고려할 만한 시나리오**: 가드레일/PII/감사 로그가 인프라 차원에서 필요할 때. 단, 별도 게이트웨이 운영 비용 감수 필요.

### Helicone — 제외

- **사유**: 주력 통합 방식이 **프록시 패턴**. OpenAI SDK 의 `base_url` 을 Helicone proxy 로 돌려 사용. async logging SDK(OpenLLMetry 기반), LangChain/LlamaIndex/Vercel AI 통합 등 보조 SDK 는 있으나, 게이트웨이 본체는 프록시 서버(호스팅 또는 자체 호스팅)에 있어 SDK 임베드만으로 완결되지 않음.
- **통신 경로**: `내 앱 + OpenAI SDK ──HTTP──▶ Helicone proxy ──HTTP──▶ provider`
- **OSS 여부**: Apache 2.0 OSS — 자체 호스팅 가능하지만 그 자체로 별도 인프라.
- **고려할 만한 시나리오**: 옵저버빌리티(로깅/비용/지연 추적)가 1차 목적이고 라우팅 로직은 따로 안 둘 때.

### OpenRouter — 제외

- **사유**: **호스팅 전용 SaaS**, 백엔드 라우터 소스 비공개, 자체 호스팅 불가. 공식 SDK(`@openrouter/sdk` TS, Python SDK, Agent SDK)가 존재하지만 모두 호스팅 엔드포인트(`openrouter.ai`)를 호출하는 클라이언트라 폐쇄망 사용 자체가 불가능.
- **통신 경로**: `내 앱 + (OpenRouter SDK 또는 OpenAI SDK) ──HTTPS──▶ openrouter.ai ──HTTP──▶ provider`
- **OSS 여부**: ❌ 백엔드 클로즈드 소스 (클라이언트 SDK 만 공개).
- **요금**: 크레딧 충전 사용분에는 자체 마진 포함, BYOK(직접 키 사용)는 월 1M 요청까지 무료·초과분 5%(향후 고정 월 구독으로 전환 예정).
- **고려할 만한 시나리오**: PoC/프로토타입 단계에서 다수 모델을 빠르게 비교할 때만.

### Bifrost — 제외

- **사유**: **Go 로 작성된 게이트웨이 서버**. Python/TS 사용자 입장에서는 OpenAI SDK 의 `base_url` 을 Bifrost 서버로 돌리는 **프록시 방식만 가능**. SDK 임베드 통합은 Go 한정. 본 저장소는 Python/TS 우선이므로 SDK 임베드 조건 미충족.
- **통신 경로**: `내 앱 + OpenAI/Anthropic SDK ──HTTP──▶ Bifrost gateway(Go) ──HTTP──▶ provider`
- **OSS 여부**: Apache 2.0 OSS — Docker/NPX 로 자체 호스팅 가능.
- **고려할 만한 시나리오**: 극단적 고성능(공식 벤치마크 기준 t3.xlarge·5000 RPS 환경에서 Bifrost 자체 오버헤드 11µs, JSON marshaling·HTTP 호출 제외; t3.medium 에서는 59µs)이 필요하고, 별도 게이트웨이 운영을 감수할 수 있는 대규모 트래픽 환경. 또는 Go 백엔드 프로젝트라면 임베드 방식으로 검토 가치 있음.

## 비교 요약

| 항목 | LiteLLM | RouteLLM | Portkey | Helicone | OpenRouter | Bifrost |
|---|---|---|---|---|---|---|
| 무료 | ✅ | ✅ | ✅ | ✅ | △(크레딧 마진/BYOK 5%) | ✅ |
| Python/TS 네이티브 SDK | ✅(Py) | ✅(Py) | ✅(Py+TS) | △(보조 logging SDK) | ✅(Py+TS) | ❌ (Go 만) |
| SDK만으로 동작 (백엔드 서비스 불요) | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ (Python/TS 기준) |
| 폐쇄망 가능 | ✅ | ✅ | △(자체 호스팅 시) | △(자체 호스팅 시) | ❌ | △(자체 호스팅 시) |
| 본 저장소 채택 | ✅ | ✅ | ❌ | ❌ | ❌ | ❌ |

## 향후 추가 가능성

본 저장소의 채택 기준은 "SDK 임베드 가능"이지만, 운영 요구사항이 달라지면 위 제외 서비스 중 일부를 별도 `examples/<service>-selfhosted/` 형태로 추가할 수 있습니다 — 예: Portkey gateway 자체 호스팅 + SDK 연결 예제.
