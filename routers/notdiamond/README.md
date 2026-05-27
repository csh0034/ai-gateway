# Not Diamond

프롬프트 단위로 어떤 모델이 최적인지 추천하는 라우터. 추천(10-100ms) 만 받고 실제 LLM 호출은 **client 측에서 본인 키로** 수행하는 구조 — 라우터를 통해 트래픽이 흐르지 않음.

> 참고: OpenRouter 의 `openrouter/auto` 가 내부적으로 Not Diamond 의 라우팅 모델을 사용한다는 보고가 있음 (즉, OpenRouter Auto Router 의 추천 엔진).

## 라이선스 / 비용

- **라이선스**: **Proprietary** (백엔드 closed source).
- **비용**: **부분 무료** — free tier 후 종량제 + 엔터프라이즈 플랜.
- **폐쇄망**: △ — 추천 API 호출은 Not Diamond 클라우드, 최종 LLM 호출은 본인 환경에서 실행되므로 LLM 호출 자체는 폐쇄망 가능.

> ⚠️ **Python SDK 동결**: [`notdiamond-python`](https://github.com/Not-Diamond/notdiamond-python) 저장소가 2025-12 에 GitHub **archived** 처리됐습니다. SaaS·API 자체의 종료를 뜻하지는 않으나(백엔드는 별개), SDK 신규 기능·버그 수정은 기대하기 어렵습니다. 도입 전 [공식 문서](https://docs.notdiamond.ai)에서 API 운영 상태를 확인하세요.

## 강점

- 추천만 받고 호출은 client 가 하므로 **데이터 잔존 통제**가 쉬움 (프롬프트가 LLM provider 직행).
- 라우팅 지연이 매우 짧음 (10-100ms).
- Python + TypeScript 네이티브 SDK 모두 제공.

## 사용 방식

| 모드 | 설명 |
|---|---|
| `chat.completions.create(...)` | Not Diamond 가 추천 + 그 모델로 직접 호출까지 한 번에 (편의 모드) |
| `model_select(...)` | 추천만 받고 호출은 본인 SDK 로 직접 — 키/네트워크를 본인이 통제 |

본 폴더 예제는 **편의 모드 `chat.completions.create`** 입니다.

## 설치 & 환경변수

### Python

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### TypeScript

```bash
cd typescript
npm install
cp .env.example .env
```

## 실행

```bash
python route.py
npm run route
```

## 참고 링크

- 공식: https://www.notdiamond.ai
- 문서: https://docs.notdiamond.ai
- Python SDK: https://github.com/Not-Diamond/notdiamond-python
- TS SDK: https://www.npmjs.com/package/notdiamond
- `model_select` vs `create`: https://docs.notdiamond.ai/docs/model_select-vs-create
