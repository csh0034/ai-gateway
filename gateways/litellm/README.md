# LiteLLM

100+ LLM provider 를 단일 OpenAI 호환 인터페이스로 호출하는 게이트웨이.

## 라이선스 / 비용

- **라이선스**: OSS. 메인 패키지는 MIT, `enterprise/` 디렉토리는 별도 상용 라이선스로 분리.
- **비용**: SDK·OSS Proxy 자체는 무료. LiteLLM Cloud / Enterprise (관리 UI, SSO, 감사 로그 등)는 유료.

## 강점

- Python 네이티브 SDK로 `litellm.completion(...)` 한 줄에 OpenAI / Anthropic / Bedrock / Vertex 등 호출.
- 동일 인터페이스에서 fallback, 재시도, 비용 추적, 가드레일 내장.
- `litellm --model ...` 으로 OpenAI 호환 proxy 서버를 띄울 수도 있음 (이 모드에서는 모든 언어가 OpenAI SDK로 접근 가능).

## 핵심 기능

- **통합 인터페이스**: 100+ provider(OpenAI / Anthropic / Bedrock / Vertex / Azure / Cohere / Ollama / vLLM 등) 를 OpenAI Chat Completions 스키마로 호출.
- **Router**: 가중치·지연·비용 기반 로드밸런싱, 모델 그룹 폴백, 재시도·쿨다운, 컨텍스트 윈도우 사전 검사.
- **비용 추적**: 호출별 `response_cost` 자동 산출, 콜백으로 키/모델/엔드포인트 단위 집계.
- **멀티모달 API**: chat 외에 embeddings, image, audio (STT/TTS), moderation 까지 동일 시그니처.
- **캐싱**: 메모리 / Redis / S3 / Disk 백엔드, 모델 그룹 간 캐시 공유.
- **옵저버빌리티**: Langfuse, Helicone, Lunary, Arize, Datadog, OpenTelemetry 등 콜백 통합.
- **가드레일**: Lakera, Bedrock Guardrails, Aporia 등 입출력 필터 후크.

## 사용 방식

LiteLLM 은 두 가지 경로로 쓸 수 있습니다. 같은 라우팅·폴백·비용 추적 코어를 공유하되, **운영 기능(가상 키, 예산, UI)** 은 Proxy 에서만 동작합니다.

| 모드 | 형태 | 적합한 케이스 | SDK 만으로 가능? |
|---|---|---|---|
| **Python SDK** | `import litellm` — 내 앱 프로세스에 임베드 | 한 앱에서 직접 LLM 호출, 라우팅·폴백·비용 추적이 목표 | ✅ |
| **Proxy / Gateway** | `litellm --config ...` 로 별도 게이트웨이 프로세스 실행 (Docker 권장) + Postgres | 여러 팀/앱에 가상 키 발급, 예산·UI·SSO 등 조직 차원 운영 | ❌ (DB·프록시 필요) |

> 본 폴더는 **SDK 모드만** 예제로 다룹니다. Proxy 가 필요하면 [공식 Quick Start](https://docs.litellm.ai/docs/proxy/quick_start) 참고.

## TypeScript 지원

LiteLLM은 **Python 네이티브 SDK만** 제공합니다. TS에서 LiteLLM의 라우팅/통합을 쓰려면 LiteLLM proxy 서버를 띄우고 OpenAI Node SDK 의 `baseURL` 을 그 서버로 가리키는 방식이어야 하므로, 이 폴더에는 Python 예제만 둡니다.

## 설치 & 환경변수

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # 후 키 채우기
```

`.env.example` 의 키 중 사용할 모델의 키만 채우면 됩니다.

## 실행

```bash
python chat.py
```

## 참고 링크

- 공식 문서: https://docs.litellm.ai
- GitHub: https://github.com/BerriAI/litellm
- 지원 provider 목록: https://docs.litellm.ai/docs/providers
- Router (로드밸런싱/폴백): https://docs.litellm.ai/docs/routing
- 비용/토큰 사용량 추적: https://docs.litellm.ai/docs/completion/token_usage
- 옵저버빌리티 콜백: https://docs.litellm.ai/docs/observability/callbacks
- Proxy 모드 (가상 키·예산·UI): https://docs.litellm.ai/docs/proxy/quick_start
- Virtual Keys (Proxy 전용): https://docs.litellm.ai/docs/proxy/virtual_keys
