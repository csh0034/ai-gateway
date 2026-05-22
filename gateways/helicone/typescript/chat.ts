import "dotenv/config";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!,
  baseURL: "https://oai.helicone.ai/v1",
  defaultHeaders: {
    "Helicone-Auth": `Bearer ${process.env.HELICONE_API_KEY!}`,
    "Helicone-Property-App": "ai-gateway-examples",
  },
});

const resp = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [
    {
      role: "user",
      content: "한 줄로 옵저버빌리티가 LLM 운영에 왜 중요한지 설명해줘.",
    },
  ],
  max_tokens: 200,
});

console.log(resp.choices[0].message.content);
