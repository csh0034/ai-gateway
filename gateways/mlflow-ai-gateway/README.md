# MLflow AI Gateway

MLflow 가 제공하는 게이트웨이 기능. LLM 호출을 MLflow 트래킹 서버와 일체화해 거버넌스(중앙 자격 증명, 정책, 감사)·옵저버빌리티를 통합 관리.

> 이력: 한때 `MLflow Deployments for LLMs` 로 이름이 바뀌고 deprecated 표시도 있었으나, 최근 deprecation 이 해제되고 AI Gateway 가 다시 정식 기능으로 유지되고 있음. MLflow 3.11+ 부터 LiteLLM 의존 없이 OpenAI / Anthropic / Bedrock / Azure / Mistral / Cohere / DeepSeek / Groq / TogetherAI / xAI / OpenRouter / Ollama / Vertex 등 native provider 지원.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0, MLflow 일부).
- **비용**: 무료 (셀프호스팅).
- **폐쇄망**: ✅ 가능.

## 강점

- MLflow 실험/모델 레지스트리/트래킹과 한 서버에서 일체 운영 → MLOps 스택이 이미 MLflow 라면 신규 인프라 0.
- MLflow 3.9.0+ 부터 게이트웨이가 트래킹 서버에 내장 — 별도 프로세스 불필요.
- provider 키를 게이트웨이가 보관, 사용자/팀은 게이트웨이 endpoint 만 알면 됨.

## 본 폴더에 코드 예제가 없는 이유

- MLflow 트래킹 서버 운영이 전제. 클라이언트 측은 `mlflow.gateway` / `mlflow.deployments` SDK 또는 OpenAI SDK 의 `base_url` 변경 패턴이라 차별성 적음.

## 사용 방식 (요약)

```yaml
# config.yaml (게이트웨이 routes 정의)
routes:
  - name: chat
    route_type: llm/v1/chat
    model:
      provider: openai
      name: gpt-4o-mini
      config:
        openai_api_key: $OPENAI_API_KEY
```

```bash
mlflow gateway start --config-path config.yaml --port 5000
```

```python
from mlflow.deployments import get_deploy_client
client = get_deploy_client("http://localhost:5000")
print(client.predict("chat", {"messages": [{"role": "user", "content": "hi"}]}))
```

## 참고 링크

- 공식: https://mlflow.org/ai-gateway
- 문서: https://mlflow.org/docs/latest/genai/governance/ai-gateway/
- GitHub: https://github.com/mlflow/mlflow
- Deployments 클라이언트: https://mlflow.org/docs/latest/llms/deployments/index.html
