# vLLM Semantic Router

vLLM 프로젝트의 의미 기반 LLM 라우터. Envoy 의 ExternalProcessor 로 동작해 **OpenAI 호환 요청을 가로채서** 비용·지연·프라이버시·안전·모달리티 기준에 따라 가장 적합한 백엔드 모델로 라우팅. 로컬·프라이빗·프런티어 모델을 혼합하는 Mixture-of-Models 시나리오를 위해 설계.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0).
- **비용**: 무료 (셀프호스팅).
- **폐쇄망**: ✅ 가능 (K8s + Envoy 환경 필요).

## 강점

- Envoy ExtProc 패턴 → 기존 Envoy AI Gateway, Istio 데이터플레인에 그대로 부착 가능.
- 의미 기반 (semantic) 분류로 단순 rule 보다 정교한 라우팅.
- 안전 / 프라이버시 등급 기반 라우팅을 1급 시민으로 다룸.

## 본 폴더에 코드 예제가 없는 이유

- 단독 Python/TS 라이브러리가 아닌 **Envoy ExtProc 서버**라서, K8s + Envoy + Gateway API 환경이 전제입니다.
- 클라이언트 측은 OpenAI SDK 그대로 사용하고 Envoy 가 라우팅을 처리합니다.

## 사용 방식 (요약)

```bash
# Envoy AI Gateway 와 결합해 K8s 에 배포
helm upgrade --install vllm-semantic-router \
  oci://ghcr.io/vllm-project/charts/vllm-semantic-router \
  -n ai-gateway
```

자세한 매니페스트는 공식 문서 참고.

## 참고 링크

- 공식 문서: https://vllm-semantic-router.com
- Envoy AI Gateway 연동: https://vllm-semantic-router.com/docs/installation/k8s/ai-gateway/
- GitHub: https://github.com/vllm-project/semantic-router
- vLLM 본체: https://github.com/vllm-project/vllm
