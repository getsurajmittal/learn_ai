import os, re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

model = "openai/gpt-oss-120b"

def get_product_price(product):
    product=product.lower().replace(" ","")
    
    if product=="iphone17" :
        return 1000
    elif product=="iphone 15" :
        return 500
    else:
        return 0

def calculator(expression):
    try:
        return eval(expression)
    except:
        return "calculation error!"

tools={
    "get_product_price":get_product_price,
    "calculator":calculator,
}

system_prompt=f'''you are a shopping assistant
you have the tools:
get_product_price(product) : returns the price in rupees
calculator(expression) : evaluates a math expression and returns result

use format, one action per reply then stop and wait
Thought:<your reasoning>
action:<tool>(<arguments>)

you will receive : <tool result>

when you know the answer, reply: final answer:<answer>

'''

user_prompt="I want to purchase an iphone17 and i have 2000 rupees after purchasing how much money will i have left?"

messages = [
    {
        "role":"system",
        "content":system_prompt,
    },
    {
        "role":"user",
        "content":user_prompt,
    }
]

for step in range(5):
    reply = client.chat.completions.create(model=model, messages=messages).choices[0].message.content

    messages.append({
        "role":"assistant",
        "content":reply
    })

    if "final answer" in reply.lower():
        print(reply)
        break

    match = re.search(r'action:\s*(\w+)\(\s*"?(.*?)"?\s*\)', reply, re.IGNORECASE)
    if not match:
        messages.append({"role": "user", "content": "Please follow the Action format."})
        continue
    
    name, arg = match.groups()
    result = tools[name](arg) if name in tools else f"Unknown tool {name}"
    messages.append({"role": "user", "content": f"Observation: {result}"})