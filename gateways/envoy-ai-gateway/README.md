# Envoy AI Gateway

Envoy Gateway (CNCF) 의 공식 AI 확장 프로젝트. Kubernetes 환경에서 Envoy 의 ExternalProcessor 패턴으로 LLM 트래픽 처리.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0). Envoy Project 산하 — CNCF 거버넌스.
- **비용**: 무료 (셀프호스팅).
- **폐쇄망**: ✅ 가능 (K8s 환경 필요).

## 강점

- CNCF 표준 라인 — Envoy / Istio 사용 조직이라면 **기존 데이터플레인에 그대로 얹어 사용** 가능.
- Gateway API (K8s) 표준 리소스로 라우팅 정의 → 인프라 코드와 통합.
- 다양한 ExtProc 구현체와 조합 가능 (예: vLLM Semantic Router 도 ExtProc 으로 동작).

## 본 폴더에 코드 예제가 없는 이유

- K8s 클러스터 + Envoy Gateway + CRD (Gateway API) 가 전제이므로, "30라인 예제" 가 성립하기 어렵습니다.
- Python / TypeScript 측은 OpenAI SDK 의 `base_url` 만 K8s Service / Ingress 로 가리키면 끝.

## 사용 방식 (요약)

```yaml
# AIGatewayRoute 리소스 예시
apiVersion: aigateway.envoyproxy.io/v1alpha1
kind: AIGatewayRoute
metadata:
  name: openai-route
spec:
  schema:
    name: OpenAI
  rules:
    - matches:
        - headers:
            - name: x-ai-eg-model
              value: gpt-4o-mini
      backendRefs:
        - name: openai-backend
```

## 참고 링크

- 공식: https://aigateway.envoyproxy.io
- GitHub: https://github.com/envoyproxy/ai-gateway
- 설치 가이드: https://aigateway.envoyproxy.io/docs/getting-started
- Envoy Gateway: https://gateway.envoyproxy.io
- vLLM Semantic Router 와의 통합: https://vllm-semantic-router.com/docs/installation/k8s/ai-gateway/
