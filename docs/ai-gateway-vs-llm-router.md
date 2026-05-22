# AI Gateway vs LLM Router

자주 혼용되지만 책임 레이어가 다르다. 그리고 **"AI Gateway"라는 단어 자체가 두 가지 의미로 쓰이기 때문에** 다이어그램에서 위치가 헷갈리는 경우가 많다. 먼저 용어부터 정리한다.

## "AI Gateway" 의 두 가지 의미

| 의미 | 별칭 | 책임 | 위치 |
|---|---|---|---|
| (A) **앞단 게이트웨이** | API Gateway, Application Gateway | 인증·요금·rate limit·감사·외부 노출 | 최전단 (사용자 ↔ 시스템 경계) |
| (B) **모델 핸들러** | Model Gateway, Model Handler, Provider 통합 SDK | provider 별 API 호출 통합, 토큰/비용 추적, fallback | 뒤쪽 (라우팅 결정 후, 실제 모델 호출 직전) |

같은 제품도 두 가지 역할을 다 하기도 한다 (예: LiteLLM proxy 는 단독 사용 시 (A)+(B) 모두 수행, KORA 같은 라우터와 결합되면 (B) 만 담당).

## 한 줄 요약

- **Proxy**: 요청을 그대로 전달하는 운송 레이어.
- **Router**: 어떤 모델/제공자에게 보낼지 결정하는 의사결정 레이어.
- **AI Gateway**: 위 (A) 또는 (B) — 문맥마다 다름.

대부분의 상용 플랫폼은 셋을 합쳐 "통합 API + 라우팅 + 정책"으로 제공한다.

## 책임 비교

| 항목 | API Gateway (A) | LLM Router | Model Gateway (B) |
|---|---|---|---|
| 1차 목적 | 외부 노출/보호 | 적합한 모델 선택 | provider 호출 통합 |
| 결정 기준 | 정책(예산, 권한, 한도) | 프롬프트 특성(난이도, 도메인) | (결정 안 함, 위임 받음) |
| 일반 기능 | 인증, 요금 추적, rate limit, 감사 | 모델 분류, 강·약모델 페어, threshold | OpenAI 호환 변환, 토큰 카운트, fallback |
| 대표 구현 | Kong, Azure APIM, Nginx | RouteLLM, NVIDIA LLM Router, KORA | LiteLLM, Portkey gateway |

## 두 가지 자주 보이는 배치 패턴

### 패턴 1 — 통합형 (간단한 시스템에서 흔함)

```
Application
   ↓
[ AI Gateway = 통합 컴포넌트 ]   ← 인증 + 라우팅 + provider 호출을 한 곳에서
   ↓
LLM Providers
```

LiteLLM proxy 단독, Portkey 단독, OpenRouter 같은 호스팅형이 여기에 해당. SDK 임베드형(`litellm.completion()` 호출)도 본질적으로 이 패턴.

### 패턴 2 — 분리형 (운영 규모 커질 때 흔함)

```
Application
   ↓
① API Gateway                   ← 일반 API 게이트웨이 (예: Azure APIM, Kong)
   ↓                              인증/감사/rate limit/외부 노출 책임
② LLM Router                    ← 모델 선택 결정
   ↓                              (Rule-based / Semantic / Static)
③ Model Gateway                 ← provider 통합 호출 (예: LiteLLM)
   ↓                              여기서 토큰/비용 추적, fallback
LLM Providers
```

이 패턴에서는 **Router 가 Model Gateway(LiteLLM 등) 앞**에 온다. "AI Gateway"라는 단어는 ① 을 가리킬 수도, ③ 을 가리킬 수도 있어 혼란이 생긴다.

### 참고: KT KORA 사례

KT 의 [KORA 아키텍처 소개 글](https://enterprise.kt.com/bt/dxstory/3691.do) 본문에는 LiteLLM 이 "사용자, LLM, 그리고 라우팅 컨트롤러 사이를 이어주는 메신저이자 관문" 으로 기술되어 있다 — 위 패턴 2와는 다르게, LiteLLM 이 라우팅 컨트롤러의 **앞단** 관문 역할로 위치한다는 읽기가 가능하다.

다만 해당 페이지는 다이어그램 위주여서 텍스트 추출만으로 박스 배치를 단정하기는 어렵다. KORA 가 분리형 패턴의 대표 사례로 자주 인용되지만, 정확한 컴포넌트 배치(특히 LiteLLM 의 위치)는 원문 다이어그램을 직접 확인하는 편이 안전하다.

## 그래서 어느 게 앞이냐?

상황별로 답이 다르다:

| 문맥 | "AI Gateway" 가 가리키는 것 | Router 대비 위치 |
|---|---|---|
| LiteLLM/Portkey 단독 사용 글 | 통합 컴포넌트 (A+B) | "Gateway 안에 라우팅 기능이 들어있다" |
| 분리형 아키텍처 글 | 보통 ① API Gateway | Gateway(①) → Router → Model Gateway(③) |
| OpenRouter 같은 호스팅 SaaS 글 | 통합 컴포넌트 (A+B) | 라우팅을 게이트웨이가 흡수 |

**기억할 패턴**: 본격적인 분리형 운영에서는 보통 **"API Gateway → Router → Model Gateway"** 순서다. 단순 OSS 통합 (LiteLLM 단독 등) 글에서는 라우팅이 게이트웨이 안에 흡수되어 있어 "Gateway 가 앞" 처럼 보일 뿐이다.

## 선택 기준

| 상황 | 추천 |
|---|---|
| 빠른 프로토타입, 다수 provider 통합 호출 | LiteLLM (Python) — 통합형, SDK 임베드 |
| 본격 운영: 외부 노출 + 정책 | 기존 API Gateway(Kong/APIM) 앞에 두고 LLM 스택은 뒤에 |
| 본격 운영: 모델 선택 자동화 | LLM Router 별도 (RouteLLM 등) + 뒤에 LiteLLM 같은 Model Gateway |
| 옵저버빌리티 우선 (비용/지연 추적) | Model Gateway 단의 로깅 활용 (LiteLLM 의 콜백 등) |

## 주의점

- Gateway 단의 fallback 과 Router 는 다른 문제다. fallback 은 "장애 시 다른 모델", Router 는 "처음부터 다른 모델".
- 학습형 Router(예: RouteLLM)는 학습된 도메인 밖에서 성능이 떨어질 수 있음 — 도메인 평가셋으로 임계값 재튜닝 필요.
- "AI Gateway" 라는 단어가 다이어그램마다 가리키는 대상이 달라 — 글을 읽을 때 "이 글이 말하는 AI Gateway 가 (A) 인지 (B) 인지 (A+B) 통합형인지" 먼저 확인.
