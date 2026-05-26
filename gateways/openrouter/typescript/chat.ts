import 'dotenv/config';
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.OPENROUTER_API_KEY!,
  baseURL: 'https://openrouter.ai/api/v1',
  defaultHeaders: {
    'HTTP-Referer': process.env.OPENROUTER_SITE_URL ?? '',
    'X-Title': process.env.OPENROUTER_APP_NAME ?? '',
  },
});

const response = await client.chat.completions.create({
  model: 'openrouter/auto',
  messages: [{ role: 'user', content: '라우터와 게이트웨이의 차이를 한 줄로.' }],
});

console.log(response.choices[0].message.content);
