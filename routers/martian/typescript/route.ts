import 'dotenv/config';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.MARTIAN_API_KEY!,
  baseURL: 'https://api.withmartian.com/v1',
});

const response = await client.chat.completions.create({
  model: 'router',
  messages: [{ role: 'user', content: '두 줄로 LLM 라우터의 역할을 설명해줘.' }],
});

console.log(response.choices[0].message.content);
