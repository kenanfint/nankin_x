from pydantic import BaseModel

class Tweet(BaseModel):
    id: int
    text: str
    in_reply_to_tweet_id: int | None
    

class Thread(BaseModel):
    tweets: list[Tweet]