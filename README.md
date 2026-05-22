# ai-gateway

AI Gateway 및 LLM Router 개념 정리 + 실제로 많이 쓰이는 서비스들의 사용 예제 모음.

## 개념 요약

- **AI Gateway**: 다수 LLM provider 앞에 두는 통합 API/프록시 레이어. 인증/요금/로깅/페일오버/가드레일을 한 곳에서 처리.
- **LLM Router**: 입력 프롬프트의 특성에 따라 가장 적합한 모델(비용·품질·지연 트레이드오프)을 선택하는 결정 레이어.
- 자세한 비교는 [`docs/ai-gateway-vs-llm-router.md`](docs/ai-gateway-vs-llm-router.md) 참고.

## 채택 기준

본 저장소는 다음 조건을 **모두** 만족하는 서비스만 다룹니다:

1. **무료** (OSS 또는 무료 사용량 호스팅)
2. **SDK 만으로 내 앱에 임베드해서 동작** — 별도 게이트웨이/프록시 프로세스 없이 SDK 함수 호출만으로 완결
3. **폐쇄망 가능** — 외부 호스팅 의존 없이 자체 LLM 백엔드 연결 가능

제외된 서비스 목록과 사유는 [`docs/excluded-services.md`](docs/excluded-services.md) 참고.

## 디렉토리 구조

```
ai-gateway/
├─ docs/                  개념 정리, 참고 링크, 제외 서비스
├─ gateways/              AI Gateway 서비스 예제
│  └─ litellm/            (Python only)
└─ routers/               LLM Router 서비스 예제
   └─ routellm/           (Python only)
```

## 채택된 서비스 (2026.05 기준)

| 카테고리 | 서비스 | 라이선스 | 언어 |
|---|---|---|---|
| Gateway | LiteLLM | OSS (MIT, `enterprise/` 디렉토리는 별도 상용) | Python only |
| Router  | RouteLLM | OSS (Apache 2.0) | Python only |

## 예제 실행 원칙

- 모든 예제는 환경변수만 채우면 즉시 실행 가능 (`.env.example` 참고).
- 실제 키는 절대 커밋하지 않습니다 (`.gitignore`에 `.env` 포함).
- Python 예제는 `requirements.txt` 로 의존성 관리.

## 기여

각 작업은 의미 단위로 개별 커밋합니다. 커밋 메시지는 한국어 사용.
새 서비스 추가 시 위 채택 기준 3개를 먼저 확인하세요.
