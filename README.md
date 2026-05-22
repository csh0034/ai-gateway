# ai-gateway

AI Gateway 및 LLM Router 개념 정리 + 실제로 많이 쓰이는 서비스들의 사용 예제 모음.

## 개념 요약

- **AI Gateway**: 다수 LLM provider 앞에 두는 통합 API/프록시 레이어. 인증/요금/로깅/페일오버/가드레일을 한 곳에서 처리.
- **LLM Router**: 입력 프롬프트의 특성에 따라 가장 적합한 모델(비용·품질·지연 트레이드오프)을 선택하는 결정 레이어.
- 자세한 비교는 [`docs/ai-gateway-vs-llm-router.md`](docs/ai-gateway-vs-llm-router.md) 참고.

## 디렉토리 구조

```
ai-gateway/
├─ docs/                  개념 정리, 참고 링크
├─ gateways/              AI Gateway 서비스 예제
│  ├─ litellm/            (Python only)
│  ├─ portkey/            (Python + TypeScript)
│  ├─ helicone/           (Python + TypeScript)
│  └─ openrouter/         (Python + TypeScript)
└─ routers/               LLM Router 서비스 예제
   └─ routellm/           (Python only)
```

각 서비스 폴더는 자체 `README.md` 와 언어별 하위 폴더(`python/`, `typescript/`)를 가집니다.

## 대상 서비스 (2026.05 기준)

| 카테고리 | 서비스 | 라이선스/비용 | 언어 지원 |
|---|---|---|---|
| Gateway | LiteLLM | OSS (MIT) | Python only (TS는 OpenAI SDK + proxy 우회) |
| Gateway | Portkey | OSS (Apache 2.0) | Python + TypeScript |
| Gateway | Helicone | OSS (Apache 2.0) | Python + TypeScript |
| Gateway | OpenRouter | 호스팅 (사용량 5% 마크업) | Python + TypeScript |
| Router  | RouteLLM | OSS (Apache 2.0) | Python only |

상용 서비스(NotDiamond, Martian, Inworld Router 등)는 이번 정리에서 제외합니다.

## 예제 실행 원칙

- 모든 예제는 환경변수만 채우면 즉시 실행 가능 (`.env.example` 참고).
- 실제 키는 절대 커밋하지 않습니다 (`.gitignore`에 `.env` 포함).
- Python 예제는 `requirements.txt`, TypeScript 예제는 `package.json` 으로 의존성 관리.

## 기여

각 작업은 의미 단위로 개별 커밋합니다. 커밋 메시지는 한국어 사용.
