import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

model = "openai/gpt-oss-120b"
system_role = "system"
prompt1 = "you are my strict office manager"
prompt2="I love you"
role="user"

message1={
    "role":system_role,
    "content":prompt1,
}

message2={
    "role":role,
    "content":prompt2,
}

messages = [message1, message2]

response = client.chat.completions.create(model=model,messages=messages,temperature=2)
response=response.choices[0].message.content

with open("response2.txt", "w", encoding="utf-8") as file:
    print(response,file=file)