import "dotenv/config";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.OPENROUTER_API_KEY!,
  baseURL: "https://openrouter.ai/api/v1",
  defaultHeaders: {
    "HTTP-Referer": process.env.OPENROUTER_APP_URL ?? "",
    "X-Title": process.env.OPENROUTER_APP_NAME ?? "",
  },
});

const PROMPT = "한 줄로 LLM 게이트웨이의 핵심 역할을 설명해줘.";

async function ask(model: string): Promise<string> {
  const resp = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: PROMPT }],
    max_tokens: 200,
  });
  return resp.choices[0].message.content ?? "";
}

for (const model of ["anthropic/claude-haiku-4-5", "openai/gpt-4o-mini"]) {
  console.log(`[${model}]\n${await ask(model)}\n`);
}
