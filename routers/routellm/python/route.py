"""RouteLLM 기본 사용 예제.

같은 프롬프트 두 개(쉬운 질의 / 어려운 질의)를 router 로 보내,
threshold 에 따라 강모델/약모델 중 어떤 게 선택됐는지 확인.

모델명 규칙: router-<router_name>-<threshold>
- router_name: "mf" (matrix factorization, 추천 기본값)
- threshold: 0.0(항상 약모델) ~ 1.0(항상 강모델)
"""

from dotenv import load_dotenv
from routellm.controller import Controller

load_dotenv()

controller = Controller(
    routers=["mf"],
    strong_model="gpt-4-1106-preview",
    weak_model="anyscale/mistralai/Mixtral-8x7B-Instruct-v0.1",
)

THRESHOLD = 0.11593  # 강모델 호출 비율을 50% 근방으로 맞추는 캘리브레이션 값 (논문 기본)
ROUTED_MODEL = f"router-mf-{THRESHOLD}"

queries = [
    "프랑스의 수도는?",  # 약모델로 충분
    "비선형 PDE의 weak solution 개념을 distribution 이론 관점에서 설명해줘.",  # 강모델 필요
]

for q in queries:
    resp = controller.chat.completions.create(
        model=ROUTED_MODEL,
        messages=[{"role": "user", "content": q}],
        max_tokens=300,
    )
    routed_to = resp.model  # RouteLLM 은 실제 호출된 모델명을 반환
    print(f"Q: {q}\n  → routed to: {routed_to}")
    print(f"  A: {resp.choices[0].message.content[:200]}...\n")
