"""Not Diamond 가 후보 중 최적 모델 추천 + 그 모델로 직접 호출."""

from dotenv import load_dotenv
from notdiamond import NotDiamond

load_dotenv()

client = NotDiamond()

result, session_id, provider = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a concise expert."},
        {"role": "user", "content": "두 줄로 merge sort 를 설명해줘."},
    ],
    model=[
        "openai/gpt-4o-mini",
        "openai/gpt-4o",
        "anthropic/claude-3-5-sonnet-20241022",
    ],
)

print("ND session:", session_id)
print("선택된 모델:", provider.model)
print("응답:", result.content)
