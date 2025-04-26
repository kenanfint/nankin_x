import asyncio
from services.openai_client import get_openai_response
from services.twitter_client import send_tweet


async def main():
    prompt = "Escreva uma hook pra um tweet"

    response_text = await get_openai_response(prompt)

    await send_tweet(response_text)

    print(response_text)


if __name__ == "__main__":
    asyncio.run(main())
