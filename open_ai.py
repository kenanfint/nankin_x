import os
import config
from openai import OpenAI

client = OpenAI(
    api_key=config.OPEN_AI_API_KEY,
)

response = client.responses.create(
    model="gpt-4.1",
    input="Qual o custo em dolares por token do gpt-4.1?"
)

print(response.output_text)
