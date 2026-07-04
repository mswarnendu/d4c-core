import ollama
import json
from llm.configs import SYSTEM_PROMPT


conversation = [
    {"role": "system", "content": SYSTEM_PROMPT}
]


def ask_llm(question):
    conversation.append({
        "role": "user",
        "content": question
    })

    response_text = ""

    stream = ollama.chat(
        model="llama3.2:3b",
        messages=conversation,
        stream=True
    )

    for chunk in stream:
        response_text += chunk["message"]["content"]

    conversation.append({
        "role": "assistant",
        "content": response_text
    })

    return json.loads(response_text)
