# 이 저장소에서의 Claude 작업 가이드

이 저장소는 AI Gateway / LLM Router 서비스들의 **사용 예제 모음**입니다. 코드는 학습/참고용입니다.

## 작성 원칙

- **응답 언어**: 한국어.
- **예제 코드는 minimal & runnable**: 환경변수만 채우면 즉시 실행되는 30라인 내외 예제를 지향.
- **키는 절대 코드/예제에 하드코딩하지 말 것**: 항상 `.env.example` 로 안내.
- **불필요한 추상화/래퍼 금지**: 학습 목적이므로 공식 SDK 호출 패턴을 그대로 노출.

## 서비스 채택 기준 (엄격, 모두 만족해야 추가)

1. **무료** (OSS 또는 무료 사용량 호스팅)
2. **SDK 만으로 내 앱에 임베드 가능** — 별도 게이트웨이/프록시 프로세스 없이 SDK 함수 호출만으로 완결되는 라이브러리여야 함
3. **폐쇄망 가능** — 외부 호스팅 의존 없이 자체 LLM 백엔드(vLLM 등)에 연결 가능

위 3개 중 하나라도 안 맞으면 추가 금지. 제외 사유는 `docs/excluded-services.md` 에 기록.

**자주 헷갈리는 케이스:**
- "OSS이고 자체 호스팅 가능"은 채택 조건이 아님 — Portkey/Helicone 처럼 별도 게이트웨이 프로세스가 필요하면 제외.
- "TS 네이티브 SDK 없으면 Python only" 로 표기.
- 상용 서비스(NotDiamond, Martian 등)는 무조건 제외.

## 서비스 폴더 구조 규칙

```
<service>/
├─ README.md       개요·강점·설치·실행·참고링크
├─ python/         requirements.txt, .env.example, *.py
└─ typescript/     (해당 서비스가 TS 네이티브 SDK 제공 시에만)
    package.json, tsconfig.json, .env.example, *.ts
```

## README 섹션 (서비스별)

1. **개요** — 1~2줄
2. **무엇이 강점인가** — bullet 3개 이하
3. **설치 & 환경변수**
4. **실행**
5. **참고 링크**

## 커밋 정책

- 서비스 추가/수정은 의미 단위로 개별 커밋.
- 커밋 메시지는 한국어. `feat(gateways): ...`, `feat(routers): ...`, `docs: ...`, `chore: ...` 등 conventional 스타일.
- `Co-Authored-By: Claude ...` 트레일러 유지.

## 새 서비스 추가 절차

1. 채택 기준 3개 확인 → 하나라도 미충족 시 `docs/excluded-services.md` 에 사유 추가.
2. `gateways/` 또는 `routers/` 아래 폴더 생성.
3. README + 언어별 예제 작성.
4. 루트 `README.md` 의 채택 서비스 표 업데이트.
5. 개별 커밋.
