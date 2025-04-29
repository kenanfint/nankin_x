import asyncio
import json
from services.openai_client import get_openai_response, get_openai_web_search
from services.twitter_client import send_tweet
from DTO.twitter import Thread

async def main():
    prompt = "crie uma thread do twitter com 2 tweets"
    
    open_ai_response = await get_openai_response(prompt)
    thread = json.loads(open_ai_response)
    data = json.loads(open_ai_response)
    thread = Thread(**data)
    
    current_tweet_id = None
    for tweet in thread.tweets:
        if tweet.in_reply_to_tweet_id is None:
            sent_tweet = await send_tweet(tweet.text)
        else:
            sent_tweet = await send_tweet(text=tweet.text, reply_tweet_id=current_tweet_id)

        current_tweet_id = sent_tweet['id']
       


if __name__ == "__main__":
    asyncio.run(main())
