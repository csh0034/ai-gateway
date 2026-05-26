# Apache APISIX (AI Gateway)

ASF (Apache Software Foundation) 정식 프로젝트인 클라우드 네이티브 API Gateway. AI 트래픽 처리용 플러그인(`ai-proxy`, `ai-prompt-guard`, `ai-rate-limiting`, `ai-prompt-template` 등) 이 모두 OSS 코어에 포함.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0, ASF 프로젝트).
- **비용**:
  - 셀프호스팅: **무료**.
  - API7 Inc. 의 매니지드/엔터프라이즈: 유료.
- **폐쇄망**: ✅ 가능.

## 강점

- AI 관련 플러그인이 **모두 OSS 무료** — Kong 처럼 핵심 AI 플러그인이 상용 티어로 빠지지 않음.
- OpenResty/Nginx 기반, etcd 로 다이나믹 설정 → 무중단 설정 변경.
- AI 외에도 일반 API Gateway 기능 (인증, rate limit, 트래픽 분기, 옵저버빌리티) 모두 제공.

## 본 폴더에 코드 예제가 없는 이유

- APISIX 도 별도 게이트웨이 프로세스(+ etcd) 운영이 전제입니다.
- Python / TypeScript 측은 OpenAI SDK 의 `base_url` 을 APISIX 로 가리키는 프록시 패턴이라 별도 예제로 둘 차별성이 적습니다.

## 사용 방식 (요약)

```yaml
# routes 설정 (etcd 또는 admin API 로 등록)
plugins:
  ai-proxy:
    auth:
      header:
        Authorization: "Bearer $OPENAI_API_KEY"
    model:
      provider: openai
      name: gpt-4o-mini
      options:
        max_tokens: 256
```

`http://apisix:9080/v1/chat/completions` 으로 OpenAI Chat Completions 스키마 그대로 호출.

## 참고 링크

- 공식: https://apisix.apache.org
- AI Gateway 페이지: https://apisix.apache.org/ai-gateway/
- GitHub: https://github.com/apache/apisix
- AI Proxy 플러그인: https://apisix.apache.org/docs/apisix/plugins/ai-proxy
- 매니지드 (API7): https://api7.ai/
