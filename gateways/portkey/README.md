# Portkey Gateway

1600+ LLM 모델을 단일 OpenAI 호환 API 로 호출하고, 가드레일·캐싱·페일오버를 게이트웨이 단에서 처리. 2026.03 프로덕션 게이트웨이가 완전 OSS 로 머지 (단일 코드베이스).

## 라이선스 / 비용

- **라이선스**: OSS. 메인 브랜치 `LICENSE` 는 **MIT** (Copyright Portkey, Inc.). 일부 외부 자료에서 2026 년 Apache 2.0 전환 의도가 언급되었으나, 본 작성 시점(2026.05) 의 main 브랜치 LICENSE 파일은 MIT — 정확한 라이선스는 사용 시점에 LICENSE 파일을 다시 확인 권장.
- **비용**:
  - 셀프호스팅(Docker 등): **무료**.
  - Portkey 호스팅 (api.portkey.ai) + 관리 UI / 가상 키 / SSO / 감사 / SLA: **유료** (freemium + 엔터프라이즈 플랜).
- **인수 진행 중**: 2026.04.30 **Palo Alto Networks 가 Portkey 인수 의도 공식 발표**. 회계 4분기(2026 여름) 클로징 예정 — 본 작성 시점에는 종결 전. 라이선스·제품 정책은 향후 변경 여지가 있으므로 공식 채널 확인 권장.

## 강점

- OpenAI 호환 단일 endpoint 로 1600+ 모델 라우팅 (`virtual_key` 추상화).
- 50+ 가드레일(PII, 컨텐츠 필터, JSON schema 등), 의미 캐시, 자동 폴백·재시도·로드밸런싱.
- Python + TypeScript 네이티브 SDK 제공, OpenAI SDK 의 `baseURL` 만 바꿔 쓰는 우회도 가능.

## 사용 방식

| 모드 | 형태 | 비고 |
|---|---|---|
| **Hosted** | `api.portkey.ai` 호출 (관리 UI / 가상 키 사용) | freemium, API 키 발급 후 즉시 사용 |
| **Self-hosted** | OSS gateway Docker / Node 로 직접 운영 | 폐쇄망 가능, UI/가상 키/조직 기능은 별도 라이선스 (또는 OSS 만으로 운영) |

본 폴더 예제는 **Hosted 호출** 기준입니다. 셀프호스팅 시 `BASE_URL` 만 자체 게이트웨이로 바꾸면 동일하게 동작합니다.

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
# Python
python chat.py

# TypeScript
npm run chat
```

## 참고 링크

- 공식 문서: https://portkey.ai/docs
- GitHub (Gateway, Apache 2.0): https://github.com/Portkey-AI/gateway
- 셀프호스팅 가이드: https://portkey.ai/docs/product/open-source/self-hosting
- 가상 키: https://portkey.ai/docs/product/ai-gateway/virtual-keys
- 가드레일: https://portkey.ai/docs/product/guardrails
