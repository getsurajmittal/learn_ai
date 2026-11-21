import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client=Groq(api_key=api_key)

model = "openai/gpt-oss-120b"
role="user"

p1 = "Hi"
p2 = "explain time travel in details"
p3 = "write a 1000 word on machine learning"

prompts =[p1,p2,p3]

for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }

    messages = [message]

    response = client.chat.completions.create(model=model,messages=messages)
    usage=response.usage
    print(f"prompt={prompt}, tokens={usage.completion_tokens}")