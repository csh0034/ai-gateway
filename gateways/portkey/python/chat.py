"""Portkey hosted 모드 기본 사용 예제.

PORTKEY_API_KEY + virtual key 조합으로 OpenAI/Anthropic 동일 인터페이스 호출.
virtual key 는 Portkey 대시보드에서 발급한 provider 매핑 식별자.
"""

import os

from dotenv import load_dotenv
from portkey_ai import Portkey

load_dotenv()

PROMPT = "한 줄로 LLM 게이트웨이의 핵심 역할을 설명해줘."


def ask(virtual_key: str, model: str) -> str:
    client = Portkey(
        api_key=os.environ["PORTKEY_API_KEY"],
        virtual_key=virtual_key,
    )
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT}],
        max_tokens=200,
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    print(
        "[gpt-4o-mini]\n",
        ask(os.environ["PORTKEY_VIRTUAL_KEY_OPENAI"], "gpt-4o-mini"),
    )
    print(
        "\n[claude-haiku-4-5]\n",
        ask(os.environ["PORTKEY_VIRTUAL_KEY_ANTHROPIC"], "claude-haiku-4-5"),
    )
