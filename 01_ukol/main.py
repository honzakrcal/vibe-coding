import os
from dotenv import load_dotenv
import openai

load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("E_INFRA_API_TOKEN"),
    base_url="https://llm.ai.e-infra.cz/v1/",
)

def ask(prompt: str) -> str:
    r = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Odpovídej stručně a česky."},
            {"role": "user", "content": prompt},
        ],
    )
    return r.choices[0].message.content

print(ask("Co je NAT?"))
