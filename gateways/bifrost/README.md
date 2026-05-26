# Bifrost

Maxim AI 가 만든 Go 기반 초저지연 LLM 게이트웨이. 공식 벤치마크 기준 5K RPS 환경에서 게이트웨이 자체 오버헤드가 11µs 수준 (JSON marshaling·HTTP 호출 제외). 1000+ 모델 통합 + 어댑티브 로드밸런서.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0).
- **비용**:
  - **셀프호스팅**: 무료 (NPX / Docker).
  - **Maxim Cloud (매니지드)**: 유료 — 관리 UI, SSO, 감사, SLA 포함.
- **폐쇄망**: ✅ 가능 (자체 호스팅 시).

## 강점

- Go 로 작성된 게이트웨이 본체, 클러스터 모드·어댑티브 로드밸런서·시맨틱 캐시·1000+ 모델.
- LiteLLM 대비 공식 벤치마크에서 자체 게이트웨이 오버헤드 수십 배 낮음 — 대용량 RPS 환경에서 의미 있음.
- OpenAI / Anthropic / Bedrock / Vertex 등 OpenAI 호환 endpoint 로 통합.

## 한계 / 본 폴더에 코드 예제가 없는 이유

- Python / TypeScript 네이티브 SDK 가 별도로 제공되지 않음 — 사용 방식은 **Bifrost 서버를 띄우고 OpenAI SDK 의 `baseURL` 을 그쪽으로 가리키는 프록시 패턴**.
- 즉 별도 게이트웨이 프로세스 운영이 전제이므로, 본 저장소는 README 만 둡니다.

## 사용 방식 (요약)

```bash
# 1. NPX 로 단일 명령 실행 (Docker 도 가능)
npx -y @maximhq/bifrost

# 2. 내 앱에서는 OpenAI SDK 의 base_url 만 Bifrost 로 변경
#    예: http://localhost:8080/v1
```

Python / TS 모두 OpenAI SDK 그대로 사용 가능합니다.

## 참고 링크

- GitHub: https://github.com/maximhq/bifrost
- 공식 문서: https://docs.getbifrost.ai
- 벤치마크: https://github.com/maximhq/bifrost#-performance
- Docker 가이드: https://docs.getbifrost.ai/getting-started/docker
