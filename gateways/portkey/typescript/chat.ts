import "dotenv/config";
import Portkey from "portkey-ai";

const PROMPT = "한 줄로 LLM 게이트웨이의 핵심 역할을 설명해줘.";

async function ask(virtualKey: string, model: string): Promise<string> {
  const client = new Portkey({
    apiKey: process.env.PORTKEY_API_KEY!,
    virtualKey,
  });
  const resp = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: PROMPT }],
    max_tokens: 200,
  });
  return resp.choices[0].message.content ?? "";
}

const openai = await ask(
  process.env.PORTKEY_VIRTUAL_KEY_OPENAI!,
  "gpt-4o-mini",
);
console.log("[gpt-4o-mini]\n", openai);

const anthropic = await ask(
  process.env.PORTKEY_VIRTUAL_KEY_ANTHROPIC!,
  "claude-haiku-4-5",
);
console.log("\n[claude-haiku-4-5]\n", anthropic);
