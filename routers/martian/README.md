# Martian

OpenAI 호환 endpoint 로 동작하는 LLM 라우터/게이트웨이. 비용·품질·신뢰성 SLA 기반으로 요청별 모델을 자동 선택하고 페일오버까지 처리. 라우팅과 호출이 한 endpoint 에서 일어나는 통합형.

## 라이선스 / 비용

- **라이선스**: **Proprietary** (백엔드 closed source). SaaS / Enterprise.
- **비용**: **부분 무료**.
  - 개발자 무료 티어: 2,500 requests.
  - 그 이상: 종량제 (모델 사용료 + 라우팅 마진).
  - Enterprise: SLA / VPC 배포 옵션.
- **폐쇄망**: △ — Enterprise VPC 배포 시 가능, 기본은 호스팅 SaaS.

## 강점

- OpenAI SDK 의 `base_url` 만 `https://api.withmartian.com/v1` 으로 바꾸면 즉시 라우팅 적용.
- 비용 상한 / willingness-to-pay 정책 / 자동 페일오버 → 운영 친화적.
- 다수 provider 카탈로그를 단일 키로 통합.

## 사용 방식

본 폴더는 OpenAI SDK + `base_url` 변경 패턴을 사용합니다. 별도 Martian 전용 SDK 는 일반 사용에 필요 없습니다.

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

- 공식: https://withmartian.com
- 문서: https://docs.withmartian.com
- GitHub 조직: https://github.com/withmartian
- LiteLLM 연동 가이드 (base_url 확인): https://docs.withmartian.com/integrations/litellm
