# AWS Bedrock

AWS 가 제공하는 매니지드 foundation model 서비스 + 게이트웨이 기능. Anthropic Claude, Meta Llama, Mistral, Cohere, Amazon Titan, Amazon Nova 등을 단일 API (Bedrock Runtime) 로 호출.

## 라이선스 / 비용

- **라이선스**: **Proprietary** (AWS 제품).
- **비용**: **종량제 유료** — 모델별 input/output 토큰 단가 ([공식 요금](https://aws.amazon.com/bedrock/pricing/)).
- **무료 티어**: 공식 무료 티어는 거의 없음. (일부 모델 limited free trial 가능)
- **폐쇄망**: △ — AWS VPC 안에서 PrivateLink 로 접근 가능, 즉 AWS 환경에서만 폐쇄망 구성 가능.

## 강점

- IAM / VPC / PrivateLink / CloudTrail / KMS 등 AWS 거버넌스 스택에 그대로 통합.
- Bedrock Agents, Guardrails, Knowledge Bases (RAG) 등 통합 기능.
- Anthropic Claude 등 1급 모델 AWS 리전 안에서 직접 호출 → 데이터 잔존 통제 용이.

## 본 폴더에 코드 예제가 없는 이유

- Bedrock 자체가 단일 게이트웨이라기보다는 AWS 매니지드 서비스이며, 호출은 `boto3` 또는 AWS SDK 로 이루어집니다. 인증·리전·IAM 설정이 코드 예제보다 환경 구성 비중이 훨씬 큽니다.
- 다른 게이트웨이(LiteLLM, Portkey, Kong AI Gateway, Cloudflare AI Gateway 등) 는 **Bedrock 을 백엔드 provider 로 등록**해 동일 인터페이스로 호출하는 패턴이 일반적입니다.

## 사용 방식 (요약)

```python
import boto3
import json

client = boto3.client("bedrock-runtime", region_name="us-east-1")
body = {"anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": "한 줄로 게이트웨이를 정의해줘."}]}
resp = client.invoke_model(modelId="anthropic.claude-3-5-sonnet-20241022-v2:0", body=json.dumps(body))
print(json.loads(resp["body"].read())["content"][0]["text"])
```

다른 게이트웨이 경유 시:

- LiteLLM: `model="bedrock/anthropic.claude-3-5-sonnet-20241022-v2:0"`
- Portkey: virtual key 에 AWS provider 등록 후 OpenAI 호환 인터페이스로 호출.
- Cloudflare AI Gateway: provider 경로를 `/aws-bedrock` 으로 사용.

## 참고 링크

- 공식: https://aws.amazon.com/bedrock/
- API 레퍼런스: https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html
- 요금: https://aws.amazon.com/bedrock/pricing/
- VPC Endpoint (PrivateLink): https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-interface-endpoints.html
- Guardrails: https://aws.amazon.com/bedrock/guardrails/
