import 'dotenv/config';
import NotDiamond from 'notdiamond';

const client = new NotDiamond({ apiKey: process.env.NOTDIAMOND_API_KEY! });

// modelSelect 는 추천만 반환 (호출은 본인 SDK 로). 자세한 시그니처는 공식 문서 참고.
const result = await client.modelSelect({
  messages: [
    { role: 'system', content: 'You are a concise expert.' },
    { role: 'user', content: '두 줄로 merge sort 를 설명해줘.' },
  ],
  llmProviders: [
    { provider: 'openai', model: 'gpt-4o-mini' },
    { provider: 'openai', model: 'gpt-4o' },
    { provider: 'anthropic', model: 'claude-3-5-sonnet-20241022' },
  ],
});

console.log(result);
