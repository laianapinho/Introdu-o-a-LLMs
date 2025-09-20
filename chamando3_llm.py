from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY") # Chave da API oficial
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um expert em história dos LLMs."},
        {"role": "user", "content": "Conte uma história sobre o desenvolvimento da Inteligência Artificial até a invenção dos LLMs."}
    ],
    temperature=0.9
)
print(completion.choices[0].message.content)