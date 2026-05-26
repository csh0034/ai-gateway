"""Cloudflare AI Gateway 의 OpenAI 호환 endpoint 로 호출."""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

account_id = os.environ["CLOUDFLARE_ACCOUNT_ID"]
gateway_id = os.environ["CLOUDFLARE_GATEWAY_ID"]

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=f"https://gateway.ai.cloudflare.com/v1/{account_id}/{gateway_id}/openai",
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "엣지 캐시의 장점을 한 줄로."}],
)

print(response.choices[0].message.content)
