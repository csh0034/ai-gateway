# RouteLLM

LMSYS의 학습 기반 LLM 라우터. 입력 질의의 난이도를 추정해 **강모델/약모델** 사이에서 자동 선택, 품질 손실을 최소화하며 비용을 줄인다.

## 강점

- 동일 인터페이스(`Controller.chat.completions.create`)에 모델명을 `router-<router>-<threshold>` 형식으로 넘기면 라우팅 적용.
- 사전 학습된 `mf` (matrix factorization), `bert`, `causal_llm`, `random` 등 여러 라우터 옵션 제공.
- threshold 로 강모델 비율을 조절. 도메인 평가셋으로 튜닝 권장.

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
- 논문: https://arxiv.org/abs/2406.18665
- 사용 가능한 라우터/벤치마크: https://github.com/lm-sys/RouteLLM#routers
