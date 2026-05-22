"""OpenRouter 통합 예제 (OpenAI SDK 사용).

같은 프롬프트를 두 모델(provider 다름)에 보내 응답을 비교한다.
HTTP-Referer / X-Title 헤더는 OpenRouter 대시보드 표시용으로 선택사항.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": os.environ.get("OPENROUTER_APP_URL", ""),
        "X-Title": os.environ.get("OPENROUTER_APP_NAME", ""),
    },
)

PROMPT = "한 줄로 LLM 게이트웨이의 핵심 역할을 설명해줘."


def ask(model: str) -> str:
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=200,
    )
    return resp.choices[0].message.content


for model in ["anthropic/claude-haiku-4-5", "openai/gpt-4o-mini"]:
    print(f"[{model}]\n{ask(model)}\n")
