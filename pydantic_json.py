import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

class Ticket(BaseModel):
    name:str
    email:str
    issue:str
schema=Ticket.model_json_schema()
response_format={
    "type":"json_object",
}

load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

text = "hello my name is suraj and my email is surajmittal27@gmail.com and my phone is 72199, my iphone is not working that i purchased just 6 months back and I love music"
prompt = f"this is a customer ticket and extract personal information as json from {text} strictly based on schema {schema}"

message1={
    "role":"system",
    "content":"you are a support executive to resolve customer tickets"
}
message2={
    "role":"user",
    "content":prompt,
}

messages = [message1,message2]

client = Groq(api_key=api_key)
model = "openai/gpt-oss-120b"
response = client.chat.completions.create(model=model,messages=messages,response_format=response_format)
response=response.choices[0].message.content

with open ("response3.txt","w",encoding="utf-8") as file:
    print(response,file=file)