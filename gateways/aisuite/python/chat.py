"""provider:model 문자열만 바꿔 다수 provider 를 한 인터페이스로 호출."""

import os

import aisuite as ai
from dotenv import load_dotenv

load_dotenv()

client = ai.Client()

for model in ["openai:gpt-4o-mini", "anthropic:claude-3-5-haiku-latest"]:
    if not os.environ.get(f"{model.split(':')[0].upper()}_API_KEY"):
        continue
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "라우터를 한 줄로 정의해줘."}],
    )
    print(f"[{model}]", response.choices[0].message.content)
