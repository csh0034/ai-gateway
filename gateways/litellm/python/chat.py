"""LiteLLM SDK 기본 사용 예제.

같은 인터페이스로 OpenAI / Anthropic 모델을 호출하고,
fallback 옵션으로 1차 모델 실패 시 자동 전환되는 패턴을 보여준다.
"""

from dotenv import load_dotenv
from litellm import completion

load_dotenv()

PROMPT = "한 줄로 LLM 게이트웨이의 핵심 역할을 설명해줘."


def ask(model: str) -> str:
    resp = completion(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=200,
    )
    return resp.choices[0].message.content


def ask_with_fallback() -> str:
    resp = completion(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=200,
        fallbacks=["claude-haiku-4-5"],
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    print("[gpt-4o-mini]\n", ask("gpt-4o-mini"), "\n")
    print("[claude-haiku-4-5]\n", ask("claude-haiku-4-5"), "\n")
    print("[fallback]\n", ask_with_fallback())
