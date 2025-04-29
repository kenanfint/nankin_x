from openai import OpenAI
import config
import asyncio
from DTO.twitter import Thread

client = OpenAI(
    api_key=config.OPEN_AI_API_KEY,
)

async def get_openai_response(prompt: str) -> str:
    response = await asyncio.to_thread(
        client.responses.parse,
        model="gpt-4.1",
        input=prompt,
        text_format=Thread,
    )
    return response.output_text

async def get_openai_web_search(prompt: str) -> str:
    response = await asyncio.to_thread(
        client.responses.create,
        model="gpt-4.1",
        tools=[{"type": "web_search_preview"}],
        input=prompt
    )
    return response.output_text
