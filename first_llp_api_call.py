import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"
role = "user"
prompt1="what does adtran do?"
prompt2="what is the average salary for a software engineer in adtran, bengaluru for a 2yr experience?"

message1 = {
    "role":role,
    "content":prompt1,
}

# message2 = {
#     "role":role,
#     "content":prompt2,
# }

messages = [message1]

response = client.chat.completions.create(model=model,messages=messages)

# answer = response.choices[0].message.content

with open("response.txt", "w", encoding="utf-8") as file:
    # print(answer, file=file)
    for index, choice in enumerate(response.choices):
        print(f"Choice {index}: {choice.message.content}", file=file)