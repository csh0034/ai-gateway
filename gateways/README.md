# Gateways

AI Gateway 서비스 사용 예제 모음.

본 저장소 채택 기준(무료 + SDK 임베드 가능 + 폐쇄망 가능)에 부합하는 서비스만 둡니다.

| 서비스 | 라이선스 | 언어 | 한 줄 강점 |
|---|---|---|---|
| [litellm](./litellm/) | OSS (MIT, `enterprise/`는 상용) | Python only | SDK 임베드로 100+ provider 통합 호출, 별도 서버 불필요 |

## 제외된 게이트웨이

Portkey, Helicone, OpenRouter 는 SDK 임베드만으로 완결되지 않거나 자체 호스팅 불가로 제외되었습니다. 상세 사유는 [`docs/excluded-services.md`](../docs/excluded-services.md) 참고.
