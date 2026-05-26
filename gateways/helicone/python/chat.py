"""OpenAI SDK 의 base_url 만 Helicone proxy 로 바꿔 사용. 호출 즉시 대시보드에 로그가 적재됨."""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ.get("HELICONE_BASE_URL", "https://oai.helicone.ai/v1"),
    default_headers={
        "Helicone-Auth": f"Bearer {os.environ['HELICONE_API_KEY']}",
    },
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "옵저버빌리티가 뭔지 한 줄로 알려줘."}],
)

print(response.choices[0].message.content)
