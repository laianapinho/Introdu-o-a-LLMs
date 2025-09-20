import getpass
import os
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
  SystemMessage("Seja um guia turístico."),
  HumanMessage("Me explique como é a vida na China!"),
]

# 1. Armazene a resposta em uma variável
response = model.invoke(messages)

# 2. Imprima o conteúdo da resposta
print(response.content)