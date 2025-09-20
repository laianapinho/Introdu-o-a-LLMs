from openai import OpenAI
import os 

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "system", "content": "Você é um jornalista."},
      {
          "role": "user",
          "content": "Em um parágrafo, conte um caso de desastre natural."
      }
  ],
  temperature=0.9 #: Este é um parâmetro que controla a criatividade da resposta. 
  #Um valor mais alto (perto de 1.0) torna a resposta mais aleatória e criativa, 
  # enquanto um valor mais baixo (perto de 0.0) a torna mais previsível e focada.
)

print(completion.choices[0].message.content)