# LiteLLM Proxy (Docker Compose)

LiteLLM proxy 를 로컬에서 빠르게 띄워보기 위한 minimal docker-compose 세트.

## 구성

- `litellm` (docker.litellm.ai/berriai/litellm:main-stable) — OpenAI 호환 게이트웨이, `:4000` 노출
- `db` (postgres:16-alpine) — 가상 키 / 예산 / Admin UI 메타데이터 저장소
- `config.yaml` — 모델 라우팅 설정 (기본: `gpt-4o-mini`, `claude-3-5-haiku`)

## 실행

```bash
cp .env.example .env   # LITELLM_MASTER_KEY, LITELLM_SALT_KEY, provider 키 채우기
docker compose up -d
```

기동 확인:

```bash
curl http://localhost:4000/health/liveliness
```

## 호출 예시

```bash
curl http://localhost:4000/v1/chat/completions \
  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "ping"}]
  }'
```

## Admin UI

`http://localhost:4000/ui` — 로그인 시 `LITELLM_MASTER_KEY` 사용.

## 주의

- `LITELLM_SALT_KEY` 는 모델 키 암호화에 쓰이므로 **첫 모델 등록 후 변경 금지** (변경 시 기존 키 복호화 불가).
- 이 compose 는 학습/로컬 검증용. 운영에서는 Postgres 영속화·백업, master key 시크릿 관리, HTTPS 종단 등이 필요.

## 참고

- Quick Start: https://docs.litellm.ai/docs/proxy/quick_start
- Docker 배포: https://docs.litellm.ai/docs/proxy/deploy
- Config 옵션: https://docs.litellm.ai/docs/proxy/configs
- Virtual Keys: https://docs.litellm.ai/docs/proxy/virtual_keys
