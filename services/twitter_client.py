import os
import asyncio
import tweepy
import config

def authenticate():
    client = tweepy.Client(
        bearer_token=config.X_BEARER_TOKEN,
        consumer_key=config.X_API_KEY,
        consumer_secret=config.X_API_KEY_SECRET,
        access_token=config.X_ACCESS_TOKEN,
        access_token_secret=config.X_ACCESS_TOKEN_SECRET
    )

    auth = tweepy.OAuth1UserHandler(
        consumer_key=config.X_API_KEY,
        consumer_secret=config.X_API_KEY_SECRET,
        access_token=config.X_ACCESS_TOKEN,
        access_token_secret=config.X_ACCESS_TOKEN_SECRET
    )
    api = tweepy.API(auth)

    return client, api


async def send_tweet(text: str = '', alt: str = '', reply_tweet_id: str | None = None) -> None:
    try:
        client, api = authenticate()

        img_name = "1.jpg"
        image_path = os.path.join(os.path.dirname(__file__), "..", "assets", "images", img_name)

        resp = await asyncio.to_thread(api.media_upload, image_path)

        await asyncio.to_thread(api.create_media_metadata, resp.media_id, alt_text=alt)

        media_ids = [resp.media_id]

        tweet = await asyncio.to_thread(
            client.create_tweet,
            text=text,
            user_auth=True,
            media_ids=media_ids,
            in_reply_to_tweet_id=reply_tweet_id
        )

        return tweet.data
    except Exception as e:
        print(f"Erro ao enviar tweet: {e}")