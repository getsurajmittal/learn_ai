import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
model = "openai/gpt-oss-120b"
client = Groq(api_key=api_key)

issues = ["technical","return and refund", "sales"]

good_system_prompt=f"you are a professional support executive agent who is tasked to classify the incoming issue amongst {issues}, your task is to only classify and not provide any unrelated support, your output is supposed to be just the class in which is issue fits or unrelated if the issue is not related to support. For example a customer product stopped working within warranty period of 6 months can be classfied under return and refund, and someone asking how to fix his marriage will be under unrelated"

bad_system_prompt="you are a support executive"

good_system_message = {
    "role":"system",
    "content":good_system_prompt,
}

bad_system_message = {
    "role":"system",
    "content":bad_system_prompt,
}

user_prompts=["I broke up with my girlfriend","my laptop is not starting","my laptop screen broke in 2 days"]

for prompt in user_prompts:
    user_message = {
        "role":"user",
        "content":prompt,
    }

    good_messages = [good_system_message,user_message]
    bad_messages = [bad_system_message,user_message]

    good_response = client.chat.completions.create(model=model,messages=good_messages).choices[0].message.content

    bad_response = client.chat.completions.create(model=model,messages=bad_messages).choices[0].message.content

    with open ("prompt_engineering_responses.txt","a",encoding="utf-8") as file:
        print(f"prompt --> {prompt}\nresponse with prompt engineering --> {good_response}\nresponse without prompt engineering --> {bad_response}",file=file)