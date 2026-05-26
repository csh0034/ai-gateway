# Portkey Gateway

1600+ LLM 모델을 단일 OpenAI 호환 API 로 호출하고, 가드레일·캐싱·페일오버를 게이트웨이 단에서 처리. 2026.04 부터 프로덕션 게이트웨이가 완전 OSS 로 머지됨.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0). 단일 코드베이스로 자체 호스팅·매니지드 모두 동작.
- **비용**:
  - 셀프호스팅(Docker 등): **무료**.
  - Portkey 호스팅 (api.portkey.ai) + 관리 UI / 가상 키 / SSO / 감사 / SLA: **유료** (freemium + 엔터프라이즈 플랜).
- **참고**: 2026 년 Palo Alto Networks 에 인수됨 — 라이선스/제품 정책은 향후 변경 여지 있음, 공식 문서 확인 권장.

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
