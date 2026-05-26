# AI Gateway vs LLM Router

자주 혼용되지만 책임 레이어가 다르다. 본 문서에서 **AI Gateway** 는 provider 통합 호출 컴포넌트(LiteLLM, Portkey, Helicone, Bifrost, OpenRouter, Cloudflare AI Gateway 등)를 의미한다. OpenAI / Anthropic / Bedrock 등 서로 다른 API 를 단일 인터페이스로 묶고 **provider 폴백 / 로드밸런싱 / 토큰·비용 추적** 을 담당하는 레이어다.

> 참고: Kong / Azure APIM / AWS 같은 **API Gateway 벤더가 자기 제품의 AI 확장을 "AI Gateway"로 부르는 경우**도 있다. 외부 자료를 읽을 때는 그 글이 말하는 "AI Gateway" 가 (a) API Gateway 의 AI 확장인지, (b) LLM provider 통합 컴포넌트인지 먼저 확인하는 편이 안전하다. 본 문서는 (b) 의 의미로 통일해 사용한다.

## 한 줄 요약

- **API Gateway**: 외부 노출·보호 레이어. 인증·rate limit·감사. 페이로드 의미 모름.
- **LLM Router**: **프롬프트 의미** 기반으로 어떤 모델에 보낼지 결정하는 의사결정 레이어.
- **AI Gateway**: provider 통합 호출 컴포넌트. 단일 인터페이스 + 토큰·비용 추적 + provider 폴백 + 로드밸런싱.

대부분의 상용 플랫폼은 셋을 합쳐 "통합 API + 라우팅 + 정책"으로 제공한다.

## 용어 주의 — 같은 단어, 다른 의미

LiteLLM 의 `Router` 클래스 / Portkey 의 "load balancing" 같은 표현은 **가중치·지연·비용 기반 로드밸런싱과 폴백**을 의미하며, 본 문서가 말하는 "LLM Router (프롬프트 의미 기반 모델 선택)" 와는 다른 개념이다.

| 표현 | 본 문서 분류 | 의미 |
|---|---|---|
| LiteLLM 의 `Router` | **AI Gateway** 의 일부 | 가중치/지연/비용 기반 로드밸런싱, 모델 그룹 폴백 |
| Portkey "load balancer" | **AI Gateway** 의 일부 | provider 간 트래픽 분배 |
| RouteLLM / Not Diamond / Martian | **LLM Router** | 입력 프롬프트의 난이도·도메인을 추정해 모델 선택 |
| OpenRouter `openrouter/auto` | **AI Gateway + LLM Router** 통합 | Not Diamond 라우터를 백엔드로 호출까지 한 곳에서 |

요점: "라우팅" 이라는 단어가 보이면 **프롬프트 의미 기반 결정인지**, **운영 메트릭(가중치/지연) 기반 분배인지** 부터 확인.

## 책임 비교

| 항목 | API Gateway | LLM Router | AI Gateway |
|---|---|---|---|
| 1차 목적 | 외부 노출/보호 | 프롬프트별 최적 모델 선택 | provider 호출 통합 |
| 결정 단위 | 요청 메타데이터 (헤더, 키, IP) | 프롬프트 페이로드 의미 | 모델 그룹·provider 운영 메트릭 |
| "결정" 이 의미하는 것 | 통과 / 거부 / 제한 | 어느 모델 / 강·약 페어 선택 | 폴백·로드밸런싱·재시도 (프롬프트 의미 결정은 ❌) |
| 일반 기능 | 인증, rate limit(req/s), 감사, mTLS | 모델 분류기, threshold, 강·약 모델 페어 | OpenAI 호환 변환, 토큰 카운트, 비용 추적, 폴백, 캐시 |
| 대표 구현 | Kong, Azure APIM, Nginx | RouteLLM, Not Diamond, Martian, vLLM Semantic Router, NVIDIA LLM Router | LiteLLM, Portkey, Helicone, Bifrost, OpenRouter, Cloudflare AI Gateway, aisuite |

## 정책 책임 매트릭스 (어디서 처리하는가)

LLM 환경의 "정책" 은 **요청 메타데이터만 봐서 되는 것** 과 **응답 페이로드의 의미를 알아야 하는 것** 으로 갈린다. 후자는 일반 API Gateway 가 직접 처리할 수 없다.

| 정책 종류 | 1차 책임 레이어 | 이유 |
|---|---|---|
| 인증 (AuthN/Z, OIDC, mTLS) | **API Gateway** | 요청 헤더만 보면 됨 |
| Rate limit (요청 수 / IP / 사용자 기준) | **API Gateway** | HTTP 메타데이터로 충분 |
| 감사 로그 (요청·응답 도착 사실 기록) | **API Gateway** | 페이로드 의미 무관 |
| 외부 노출 / WAF / DDoS | **API Gateway** | 네트워크 레이어 |
| **예산 (USD 한도, 월/팀/키별)** | **AI Gateway** | 응답에서 토큰 수·모델 단가를 알아야 산정 가능 |
| **토큰 단위 한도 (TPM, 컨텍스트 길이 제한)** | **AI Gateway** | provider 응답을 파싱해야 카운트 가능 |
| **모델 화이트/블랙리스트** | **AI Gateway** | 모델 식별자는 LLM 페이로드 안 |
| **가드레일 (PII, 컨텐츠 필터, JSON schema)** | **AI Gateway** | 페이로드 본문 검사 필요 |
| **의미 캐시 (semantic cache)** | **AI Gateway** | 프롬프트 임베딩 비교 필요 |

> Kong AI Gateway, Apache APISIX, Envoy AI Gateway 처럼 **API Gateway 가 AI 확장을 흡수한 제품군**은 한 프로세스가 두 영역을 모두 처리한다. 이때도 본질은 같다 — 요청 수준 정책은 페이로드 모르고도 가능, 토큰/비용 정책은 페이로드 파싱 필수.

## 두 가지 자주 보이는 배치 패턴

### 패턴 1 — 통합형 (간단한 시스템에서 흔함)

```
Application
   ↓
[ AI Gateway = 통합 컴포넌트 ]   ← 라우팅·폴백·비용 추적·(선택) 가상 키 발급
   ↓
LLM Providers
```

LiteLLM proxy 단독, Portkey 단독, OpenRouter 같은 호스팅형이 여기에 해당. SDK 임베드형 (`litellm.completion()`, `client.chat.completions.create()`) 도 본질적으로 동일 — 외부 노출이 없으니 API Gateway 책임이 빠지고 AI Gateway 가 운영 기능 전부 흡수.

### 패턴 2 — 분리형 (운영 규모 커질 때 흔함)

```
Application
   ↓
① API Gateway        ← 인증 / 감사 / 요청-단위 rate limit / 외부 노출
   ↓
② LLM Router         ← 프롬프트 의미 기반 모델 선택
   ↓                   (Rule-based / Semantic / Learning-based)
③ AI Gateway         ← provider 호출 통합 / 토큰·비용 한도 / 폴백 / 캐시
   ↓
LLM Providers
```

이 배치에서는 **Router 가 AI Gateway 앞**에 온다. "토큰 한도" 같은 LLM 정책은 ③ 에서, "요청 한도 / 인증" 은 ① 에서 — 책임이 분리된다.

#### 변형: LLM Gateway 가 라우터 앞에 오는 케이스 (KT KORA)

KT 의 [KORA 아키텍처 소개](https://enterprise.kt.com/bt/dxstory/3691.do) 본문은 LiteLLM 을 "사용자, LLM, 그리고 라우팅 컨트롤러 사이를 이어주는 메신저이자 관문" 으로 기술한다. 즉 LiteLLM 이 **라우팅 컨트롤러의 앞단** 관문 역할로 위치한다는 읽기가 가능하다.

다만 해당 페이지는 다이어그램 위주여서 텍스트만으로 박스 배치를 단정하긴 어렵다 — 원문 다이어그램 직접 확인 권장.

### "정답 배치" 는 없다

위 두 패턴 중 어느 쪽이 정석이라고 단정하기 어렵다. KORA 처럼 LLM Gateway 가 앞에 오면 "모든 LLM 트래픽이 단일 관문을 지나는" 운영 단순성을 얻고, 패턴 2 의 정석 배치면 "각 레이어 책임이 명확" 한 이점을 얻는다. 조직 운영 모델에 맞춰 선택하면 된다.

## 선택 기준

| 상황 | 추천 |
|---|---|
| 빠른 프로토타입, 다수 provider 통합 호출 | LiteLLM (Python SDK) 또는 aisuite (Python SDK), 단일 키 SaaS 면 OpenRouter |
| 본격 운영: 가상 키 / 예산 / UI / SSO | Portkey 또는 LiteLLM Proxy |
| 본격 운영: 외부 노출 + 토큰-단위 정책 한 곳에서 | Kong AI Gateway / Apache APISIX / Envoy AI Gateway (API Gateway 가 AI 정책까지 흡수) |
| 본격 운영: 모델 선택 자동화 | LLM Router 별도 (RouteLLM / Not Diamond / Martian / vLLM Semantic Router) + 뒤에 AI Gateway |
| 옵저버빌리티 우선 (비용/지연 추적) | Helicone (⚠️ maintenance mode), Cloudflare AI Gateway, Portkey |

## 주의점

- **폴백 ≠ 라우팅**. AI Gateway 의 폴백은 "호출 실패 시 다른 모델로 재시도", LLM Router 의 라우팅은 "처음부터 어떤 모델에 보낼지 결정". 책임 시점이 다르다.
- **로드밸런싱 ≠ LLM 라우팅**. LiteLLM `Router` / Portkey load balancer 가 하는 가중치·지연 기반 분배는 AI Gateway 영역. 프롬프트 의미를 보고 결정하는 LLM Router 와는 다름.
- **학습형 Router (RouteLLM, Not Diamond 등) 는 학습 도메인 밖에서 성능이 떨어짐** — 운영 도메인 평가셋으로 임계값 재튜닝 필요.
- **AI Gateway 단의 비용 추적은 호출 시점 단가 기준** — provider 가 단가를 변경하면 게이트웨이 메타데이터도 동기화해야 정확.
