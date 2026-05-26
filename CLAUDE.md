# 이 저장소에서의 Claude 작업 가이드

이 저장소는 AI Gateway / LLM Router 서비스들의 **사용 예제 모음**입니다. 코드는 학습/참고용입니다.

## 작성 원칙

- **응답 언어**: 한국어.
- **예제 코드는 minimal & runnable**: 환경변수만 채우면 즉시 실행되는 30라인 내외 예제를 지향.
- **키는 절대 코드/예제에 하드코딩하지 말 것**: 항상 `.env.example` 로 안내.
- **불필요한 추상화/래퍼 금지**: 학습 목적이므로 공식 SDK 호출 패턴을 그대로 노출.

## 서비스 선정 방침

채택 기준은 별도로 두지 않습니다. 후보 서비스는 자유롭게 추가하되, **다음 두 축은 반드시 명시**합니다:

1. **비용 구분** — `무료 / 유료 / 부분 무료 (free tier 또는 BYOK)`
2. **라이선스 구분** — `OSS (MIT / Apache 2.0 / 기타)` 또는 `Proprietary / Closed source` 등

같은 서비스라도 OSS 셀프호스팅은 무료, 호스팅/매니지드는 유료처럼 **모드별 라이선스·비용이 갈리는 경우** 가 많으므로 각 README 에 정확히 표기합니다.

## 서비스 폴더 구조 규칙

```
<service>/
├─ README.md       개요·강점·라이선스/비용·설치·실행·참고링크
├─ python/         requirements.txt, .env.example, *.py   (코드 예제가 가능한 경우)
└─ typescript/     package.json, tsconfig.json, .env.example, *.ts   (해당 서비스가 TS 네이티브 SDK 제공 시)
```

- 코드 예제가 가능한 경우(SDK 임베드 또는 OpenAI 호환 endpoint 단순 호출)만 `python/`·`typescript/` 디렉토리를 둡니다.
- **별도 게이트웨이 프로세스/K8s/대규모 인프라가 필요한 서비스** (Bifrost, Kong, Apache APISIX, Envoy AI Gateway 등)는 README 만 둡니다.

## README 섹션 (서비스별)

1. **개요** — 1~2줄
2. **라이선스 / 비용** — OSS/Proprietary, 무료/유료, 부분 무료 여부 명시
3. **강점** — bullet 3개 이하
4. **사용 방식** — SDK / Proxy / 서버 등 어떤 모드가 있고 본 폴더는 어느 모드를 다루는지
5. **설치 & 환경변수** — 코드 예제가 있는 경우만
6. **실행** — 코드 예제가 있는 경우만
7. **참고 링크**

## 커밋 정책

- 서비스 추가/수정은 의미 단위로 개별 커밋.
- 커밋 메시지는 한국어. `feat(gateways): ...`, `feat(routers): ...`, `docs: ...`, `chore: ...` 등 conventional 스타일.
- `Co-Authored-By: Claude ...` 트레일러 유지.

## 새 서비스 추가 절차

1. `gateways/` 또는 `routers/` 아래 폴더 생성.
2. README 에 라이선스 / 비용 / 강점 / 사용 방식 명시.
3. SDK 임베드나 OpenAI 호환 endpoint 단순 호출이 가능하면 `python/`·`typescript/` 예제 추가, 아니면 README 만.
4. 루트 `README.md`, `gateways/README.md`, `routers/README.md` 표 업데이트.
5. 개별 커밋.
