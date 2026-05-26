import 'dotenv/config';
import OpenAI from 'openai';

const accountId = process.env.CLOUDFLARE_ACCOUNT_ID!;
const gatewayId = process.env.CLOUDFLARE_GATEWAY_ID!;

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!,
  baseURL: `https://gateway.ai.cloudflare.com/v1/${accountId}/${gatewayId}/openai`,
});

const response = await client.chat.completions.create({
  model: 'gpt-4o-mini',
  messages: [{ role: 'user', content: '엣지 캐시의 장점을 한 줄로.' }],
});

console.log(response.choices[0].message.content);
