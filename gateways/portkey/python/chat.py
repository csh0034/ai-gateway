"""Portkey 공식 SDK 로 단일 호출. virtual_key 로 provider 키를 게이트웨이에 위임."""

import os

from dotenv import load_dotenv
from portkey_ai import Portkey

load_dotenv()

client = Portkey(
    api_key=os.environ["PORTKEY_API_KEY"],
    virtual_key=os.environ["PORTKEY_VIRTUAL_KEY"],
    base_url=os.environ.get("PORTKEY_BASE_URL"),  # 셀프호스팅 시에만 지정
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "한 줄로 게이트웨이의 정의를 알려줘."}],
)

print(response.choices[0].message.content)
