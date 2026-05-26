# Routers

LLM Router 서비스 사용 예제 모음. 라우터는 입력 프롬프트의 특성을 보고 어떤 모델로 보낼지 **결정**하는 레이어로, Gateway 와는 책임이 다릅니다 (자세한 비교는 [`docs/ai-gateway-vs-llm-router.md`](../docs/ai-gateway-vs-llm-router.md) 참고).

| 서비스 | 라이선스 | 비용 | 모드 | 코드 예제 | 한 줄 강점 |
|---|---|---|---|---|---|
| [routellm](./routellm/) | Apache 2.0 | 무료 | Python SDK (Controller) | ✅ | LMSYS 학습 기반 라우터, 강/약모델 페어로 비용 ↓ |
| [martian](./martian/) | Proprietary (백엔드 closed) | 부분 무료 (개발자 2,500 req 무료, 이후 종량제) | OpenAI 호환 SaaS | ✅ | 비용/품질 SLA, willingness-to-pay 정책, 자동 페일오버 |
| [notdiamond](./notdiamond/) | Proprietary | 부분 무료 (free tier + 유료) | Python + TS SDK (라우팅 추천 + 자체 호출) | ✅ | 프롬프트별 모델 추천(10~100ms), client-side 실행 |
| [vllm-semantic-router](./vllm-semantic-router/) | Apache 2.0 | 무료 | Envoy ExtProc 서버 (K8s) | ❌ | Mixture-of-Models 의미 기반 라우팅, vLLM 생태계 |
| [nvidia-llm-router](./nvidia-llm-router/) | MIT (소스) + 모델별 별도 라이선스 | 무료 (NIM 호스팅 비용 별도) | NIM + Triton 서버 | ❌ | NVIDIA 공식 Blueprint, 복잡도/태스크 분류기 모델 동봉 |

## 책임 비교 요약

- **순수 라우터**: RouteLLM, vLLM Semantic Router, NVIDIA LLM Router — 모델 선택만 담당, 실제 호출은 별도 게이트웨이/SDK 에 위임.
- **라우터 + 게이트웨이 통합형**: Martian, OpenRouter `auto` — 추천과 호출이 한 endpoint 에서 일어남.
- **추천 전용 (호출은 client)**: Not Diamond — 라우팅 결정만 받아서 자체 키로 호출.

## 도메인 튜닝 주의

학습형 라우터(RouteLLM, NVIDIA, Not Diamond)는 학습 도메인 밖에서 성능이 떨어질 수 있습니다. 운영 도메인 평가셋으로 threshold 재조정이 필요합니다.
