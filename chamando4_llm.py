import uuid
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

model = ChatOpenAI(model="gpt-4o-mini")

workflow = StateGraph(state_schema=MessagesState)

def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": [response]}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

thread_id = uuid.uuid4()
config = {"configurable": {"thread_id": str(thread_id)}}

query = "Olá, eu sou a Laiana e tenho 23 anos!"
input_messages = [HumanMessage(query)]

output = app.invoke({"messages": input_messages}, config=config)
output["messages"][-1].pretty_print()

query = "Quantos anos eu tenho?"
input_messages = [HumanMessage(query)]

output = app.invoke({"messages": input_messages}, config=config)
output["messages"][-1].pretty_print()