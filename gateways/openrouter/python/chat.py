"""OpenRouter 는 OpenAI 호환 endpoint. SDK 그대로 두고 base_url 만 바꿔 사용."""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
    default_headers={
        "HTTP-Referer": os.environ.get("OPENROUTER_SITE_URL", ""),
        "X-Title": os.environ.get("OPENROUTER_APP_NAME", ""),
    },
)

response = client.chat.completions.create(
    model="openrouter/auto",  # auto router. 구체 모델: "openai/gpt-4o-mini" 등
    messages=[{"role": "user", "content": "라우터와 게이트웨이의 차이를 한 줄로."}],
)

print(response.choices[0].message.content)
