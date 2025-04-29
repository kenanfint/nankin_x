import asyncio
from services.openai_client import get_openai_response, get_openai_web_search
from services.twitter_client import send_tweet


async def main():
    prompt = "Procure na web historias que dariam muita view no twitter, e me de separado em blocos de tweet, como uma thread, é interessante você me retornar midias de video ou imagem que você achar interessante em cada bloco de tweet, mas so se vc achar interessante colocar, nn precisa colocar midia em todo tweet so se achar interessante"

    response_text = await get_openai_response(prompt)
    #response_web_search = await get_openai_web_search(prompt)
    #await send_tweet(response_text)

    print(response_text)


if __name__ == "__main__":
    asyncio.run(main())
