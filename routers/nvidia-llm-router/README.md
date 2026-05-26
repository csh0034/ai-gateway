# NVIDIA LLM Router (AI Blueprint)

NVIDIA 가 공개한 LLM 라우터 reference 아키텍처. 입력 프롬프트의 **복잡도(Complexity)** 와 **태스크(Task Qualifier)** 를 작은 분류 모델로 판별해 적합한 모델로 라우팅. NIM(NVIDIA Inference Microservices) + Triton 기반.

## 라이선스 / 비용

- **라이선스 (분리)**:
  - 소스 코드 (라우터 구현체): MIT.
  - 분류기 모델 (Complexity / Task Qualifier): NVIDIA Open Model License.
  - 라우팅 대상 모델: NVIDIA AI Foundation Models Community License + 모델별 라이선스.
- **비용**:
  - 소스 사용 자체는 무료.
  - 실제 운영 시 GPU + NIM 호스팅 비용 발생 (자체 인프라 또는 NVIDIA Cloud Functions / DGX Cloud).
- **폐쇄망**: ✅ 가능 (자체 GPU + NIM 컨테이너로 폐쇄망 배포).

## 강점

- NVIDIA 공식 reference — Triton / NIM / NeMo 와 자연스럽게 결합.
- 분류기 모델이 사전 학습된 상태로 공개되어 학습 비용 0 부터 시작 가능.
- "어떤 모델로 보낼지" 를 두 분류기(난이도 + 태스크) 로 나눈 구조라 도메인 튜닝 포인트가 명확.

## 본 폴더에 코드 예제가 없는 이유

- 라우터·분류기·대상 모델이 모두 **NIM 컨테이너 서버**로 실행되어야 하며, GPU + Triton + NIM 의존성이 있어 30라인 예제 형태로는 재현 불가합니다.
- 제공되는 Jupyter notebook (`1_Deploy_LLM_Router.ipynb`) 으로 deployment 흐름을 따라가는 것이 표준 경로입니다.

## 사용 방식 (요약)

```bash
git clone https://github.com/NVIDIA-AI-Blueprints/llm-router
cd llm-router/launchable
# Jupyter 노트북 실행: 1_Deploy_LLM_Router.ipynb
```

배포 후에는 OpenAI 호환 endpoint 로 호출.

## 참고 링크

- Blueprint 공식: https://build.nvidia.com/nvidia/llm-router
- GitHub: https://github.com/NVIDIA-AI-Blueprints/llm-router
- 한국어 소개: https://developer.nvidia.com/ko-kr/blog/deploying-the-nvidia-ai-blueprint-for-cost-efficient-llm-routing/
- NIM 소개: https://www.nvidia.com/en-us/ai/nim/
