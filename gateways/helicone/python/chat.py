"""Helicone proxy 통합 예제 (OpenAI SDK 사용).

base_url 만 Helicone endpoint 로 바꾸고 Helicone-Auth 헤더를 추가하면
모든 요청이 Helicone 대시보드에 로깅된다.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url="https://oai.helicone.ai/v1",
    default_headers={
        "Helicone-Auth": f"Bearer {os.environ['HELICONE_API_KEY']}",
        # 옵션: 대시보드 필터링용 메타데이터
        "Helicone-Property-App": "ai-gateway-examples",
    },
)

resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "한 줄로 옵저버빌리티가 LLM 운영에 왜 중요한지 설명해줘."}],
    max_tokens=200,
)
print(resp.choices[0].message.content)
