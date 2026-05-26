import 'dotenv/config';
import Portkey from 'portkey-ai';

const portkey = new Portkey({
  apiKey: process.env.PORTKEY_API_KEY!,
  virtualKey: process.env.PORTKEY_VIRTUAL_KEY!,
  baseURL: process.env.PORTKEY_BASE_URL,
});

const response = await portkey.chat.completions.create({
  model: 'gpt-4o-mini',
  messages: [{ role: 'user', content: '한 줄로 게이트웨이의 정의를 알려줘.' }],
});

console.log(response.choices[0].message.content);
