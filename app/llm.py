
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from app.tools import (
    get_all_tasks,
    create_task,
    update_task,
    delete_task,
)


load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
)


class AIResponse(BaseModel):
    answer: str = Field(description="Detailed answer")
    summary: str = Field(description="Short summary")



agent = create_agent(
    model=llm,
    tools=[
    get_all_tasks,
    create_task,
    update_task,
    delete_task,],
    system_prompt=(
    "You are a helpful AI task management assistant. "
    "Use the available tools to retrieve or modify real task records. "
    "Never invent task IDs, task details, statuses, or API results. "
    "Use get_all_tasks to list tasks and get_task_by_id for a specific task. "
    "Use create_task to create a new task. "
    "Use update_task for partial updates and replace_task for full replacements. "
    "Use delete_task only when the user explicitly requests deletion. "
    "If the intended task is ambiguous, ask the user to clarify. "
    "Check tool results before claiming an operation succeeded. "
    "Explain results in simple English."
    ),
)



question = input("Ask Question...\n")

result = agent.invoke({
    "messages": [
        {"role": "user", "content": question}
    ]
})

answer = result["messages"][-1].content

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "Convert the supplied answer into the required structure. "
        "The answer field must contain the complete response. "
        "The summary field must contain a short summary. "
        "Do not invent or alter task information."
    ),
    ("human", "{answer}"),
])

messages = prompt.format_messages(answer=answer)

structured_llm = llm.with_structured_output(AIResponse)

response = structured_llm.invoke(messages)

print("\n--- Final Answer ---")
print(response.answer)

print("\n--- Summary ---")
print(response.summary)

