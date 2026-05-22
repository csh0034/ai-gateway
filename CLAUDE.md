# 이 저장소에서의 Claude 작업 가이드

이 저장소는 AI Gateway / LLM Router 서비스들의 **사용 예제 모음**입니다. 코드는 학습/참고용입니다.

## 작성 원칙

- **응답 언어**: 한국어.
- **예제 코드는 minimal & runnable**: 환경변수만 채우면 즉시 실행되는 30라인 내외 예제를 지향.
- **키는 절대 코드/예제에 하드코딩하지 말 것**: 항상 `.env.example` 로 안내.
- **불필요한 추상화/래퍼 금지**: 학습 목적이므로 공식 SDK 호출 패턴을 그대로 노출.
- **TS 네이티브 SDK 없는 서비스는 TS 예제를 만들지 않음** — README에 "Python only" 명시.
- **상용 서비스 추가 금지** — 무료 OSS 또는 무료 사용량 호스팅만.

## 서비스 폴더 구조 규칙

각 서비스 폴더는 다음 구조를 따릅니다:

```
<service>/
├─ README.md       개요·강점·설치·실행·참고링크
├─ python/         (필수) requirements.txt, .env.example, *.py
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

1. 무료 여부 확인 → 무료가 아니면 추가하지 않음.
2. 공식 SDK 언어 지원 확인 → TS 네이티브 없으면 Python only.
3. `gateways/` 또는 `routers/` 아래 폴더 생성.
4. README + 언어별 예제 작성.
5. 루트 `README.md` 의 대상 서비스 표 업데이트.
6. 개별 커밋.
