from openai import OpenAI
import config
import asyncio

client = OpenAI(
    api_key=config.OPEN_AI_API_KEY,
)

async def get_openai_response(prompt: str) -> str:
    response = await asyncio.to_thread(
        client.responses.create,
        model="gpt-4.1",
        input=prompt
    )
    return response.output_text
