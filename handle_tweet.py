import os
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

        #res = client.get_me()

        return client, api

def send_tweet(text='Doggy', alt=''):
        try:
                (client, api) = authenticate()
                
                img_name = "1.jpg"
                media_ids = []
                resp = api.media_upload(
                       os.path.join(os.path.dirname(__file__), "assets", "images", img_name)
                )

                api.create_media_metadata(resp.media_id, alt_text=alt)

                media_ids.append(resp.media_id)

                tweet = client.create_tweet(text=text, user_auth=True, media_ids=media_ids)
                
                client.create_tweet(
                        text='reply', user_auth=True, media_ids=media_ids, in_reply_to_tweet_id=tweet.data["id"]
                )
                
                print('done')
        except Exception as e:
                print(e)
        return None

print(send_tweet())