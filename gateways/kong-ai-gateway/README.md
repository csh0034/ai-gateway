# Kong AI Gateway

Kong API Gateway 의 AI 확장. 기존 Kong Nginx/OpenResty 기반 위에 AI 플러그인(AI Proxy, AI Rate Limiting, AI Semantic Caching 등)을 추가해 LLM 트래픽을 처리.

## 라이선스 / 비용

- **라이선스**: 분리.
  - **Kong Gateway OSS**: Apache 2.0 — `ai-proxy` 등 핵심 AI 플러그인 일부 포함.
  - **Kong Gateway Enterprise / Konnect SaaS**: 상용 라이선스 — 고급 AI 플러그인 (semantic caching, token-aware rate limit, prompt guards, RAG 인젝션 등), OIDC, 분석, GUI.
- **비용**:
  - OSS 자체 호스팅: 무료.
  - Konnect SaaS: 서비스당 약 $105/월~ + 사용량 (2026.05 시점).
  - Enterprise: 별도 견적, 연간 수만 달러 단위.
- **2026 주의**: Kong Gateway 3.10+ 부터 라이선스 없이 실행 시 "만료된 Enterprise 라이선스" 로 간주되어 일부 기능이 제한됨. 순수 OSS 사용은 OSS 배포본 사용을 확인할 것.
- **폐쇄망**: ✅ 가능 (OSS / Enterprise 모두 자체 호스팅).

## 강점

- 기존 Kong API Gateway 운영팀이라면 학습 곡선이 거의 0 — 플러그인 추가로 AI 트래픽 처리 가능.
- OIDC / mTLS / FIPS / 감사 등 엔터프라이즈 보안 기능을 그대로 활용.
- 멀티 데이터플레인 / 멀티 리전 운영 패턴이 이미 표준화되어 있음.

## 본 폴더에 코드 예제가 없는 이유

- Kong AI Gateway 는 본질적으로 **별도 게이트웨이 프로세스** (Nginx 기반 Kong 서버 + 데이터플레인) 운영이 전제입니다.
- Python / TypeScript 측에서는 OpenAI SDK 의 `base_url` 을 Kong 으로 가리키는 프록시 패턴만 사용하므로 별도 코드 예제로 둘 만큼의 차별성이 없습니다.

## 사용 방식 (요약)

```yaml
# kong.yml (declarative config 예시)
services:
  - name: openai-proxy
    url: https://api.openai.com
    routes:
      - name: openai-route
        paths: ["/v1/chat/completions"]
    plugins:
      - name: ai-proxy
        config:
          route_type: llm/v1/chat
          model:
            provider: openai
            name: gpt-4o-mini
```

내 앱에서는 OpenAI SDK 의 `base_url` 을 Kong 게이트웨이로 변경합니다.

## 참고 링크

- 공식: https://konghq.com/products/kong-ai-gateway
- GitHub (Kong OSS): https://github.com/Kong/kong
- AI Proxy 플러그인: https://docs.konghq.com/hub/kong-inc/ai-proxy/
- 라이선스 정책 변경 (3.10+): https://docs.konghq.com/gateway/latest/licenses
- Konnect 요금: https://konghq.com/pricing
