"""Martian OpenAI 호환 endpoint 로 라우팅. model 에 'router' 또는 구체 모델명."""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["MARTIAN_API_KEY"],
    base_url="https://api.withmartian.com/v1",
)

response = client.chat.completions.create(
    model="router",  # Martian 의 동적 라우터. 구체 모델 호출도 가능
    messages=[{"role": "user", "content": "두 줄로 LLM 라우터의 역할을 설명해줘."}],
)

print(response.choices[0].message.content)
