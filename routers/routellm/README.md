# RouteLLM

LMSYS의 학습 기반 LLM 라우터. 입력 질의의 난이도를 추정해 **강모델/약모델** 사이에서 자동 선택, 품질 손실을 최소화하며 비용을 줄인다.

## 라이선스 / 비용

- **라이선스**: OSS (Apache 2.0).
- **비용**: 무료. (강/약모델 호출 자체에는 각 provider 의 사용료 발생)

## 강점

- 동일 인터페이스(`Controller.chat.completions.create`)에 모델명을 `router-<router>-<threshold>` 형식으로 넘기면 라우팅 적용.
- 사전 학습된 `mf` (matrix factorization), `bert`, `causal_llm`, `random` 등 여러 라우터 옵션 제공.
- threshold 로 강모델 비율을 조절. 도메인 평가셋으로 튜닝 권장.

## 핵심 기능

- **이중 모델 라우팅**: 입력 난이도 추정 후 `strong_model` / `weak_model` 두 모델 사이에서 자동 선택.
- **사전 학습 라우터**: `mf`, `bert`, `causal_llm`, `sw_ranking` (+ baseline `random`) — Chatbot Arena 선호도 데이터로 학습.
- **임계값 calibration**: threshold 파라미터로 강모델 호출 비율 직접 조정, 도메인 평가셋 기반 calibration 스크립트 제공.
- **모델 자유 조합**: 강/약 모델로 임의의 OpenAI 호환 endpoint 지정 가능 (LiteLLM 백엔드를 통해 100+ provider 접근).
- **OpenAI 호환 서버 모드**: `python -m routellm.openai_server` 로 띄우면 다른 언어/도구도 라우팅 사용 가능.
- **평가 벤치마크 내장**: MT Bench, MMLU, GSM8K — 논문 기준 GPT-4 성능의 95% 를 유지하며 비용 최대 85% 절감 보고.

## 사용 방식

RouteLLM 은 두 가지 경로로 쓸 수 있습니다. 라우터 코어는 동일하고, 클라이언트 인터페이스만 다릅니다.

| 모드 | 형태 | 적합한 케이스 | SDK 만으로 가능? |
|---|---|---|---|
| **Controller (SDK)** | `Controller(...)` 객체로 직접 호출 — Python 앱에 임베드 | Python 앱에서 자체 라우팅 적용, 최소 의존 | ✅ |
| **OpenAI 호환 서버** | `python -m routellm.openai_server ...` 로 HTTP 서버 실행 | 다른 언어/도구가 OpenAI SDK 의 `baseURL` 만 바꿔 사용 | ❌ (별도 프로세스) |

> 본 폴더는 **Controller 모드만** 예제로 다룹니다. 서버 모드는 다언어 통합이 필요할 때 검토할 수 있는 경로입니다.

## TypeScript 지원

RouteLLM 은 **Python 패키지만 제공**합니다. TS 에서 사용하려면 RouteLLM 을 server 형태로 띄우고 (LiteLLM proxy 와 호환되는 형태로 동작) OpenAI SDK 의 baseURL 을 그쪽으로 가리키는 우회가 필요해, 이 폴더는 Python 예제만 둡니다.

## 설치 & 환경변수

```bash
cd python
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

약모델 호스팅은 예제에서 Anyscale 또는 Together 등 OpenAI 호환 endpoint 를 사용. 환경변수에 키만 채우면 됩니다.

## 실행

```bash
python route.py
```

## 참고 링크

- GitHub: https://github.com/lm-sys/RouteLLM
- 논문 (RouteLLM, ICLR 2025): https://arxiv.org/abs/2406.18665
- LMSYS 발표 블로그: https://www.lmsys.org/blog/2024-07-01-routellm/
- 사용 가능한 라우터/벤치마크: https://github.com/lm-sys/RouteLLM#routers
- 사전학습 라우터 가중치 (HuggingFace): https://huggingface.co/routellm
