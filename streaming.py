import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)
model = "openai/gpt-oss-120b"

message = {
    "role":"user",
    "content":"explain how internet works in 100 lines"
}

messages = [message]

response = client.chat.completions.create(model=model, messages=messages, stream=True)

for chunk in response:
    content = chunk.choices[0].delta.content
    if content:
        print(content,end="",flush=True)


# print(response)