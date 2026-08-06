import json

from openai import OpenAI

from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_ai(messages):

    response = client.responses.create(
        model="gpt-5.5",
        instructions="""
    You are an AI assistant.

    If the user wants to save a note, respond ONLY in JSON.

    Example:

    {
        "action": "save_note",
        "note": "Buy chicken"
    }

    If the user is just asking a normal question, respond with:

    {
        "action": "respond",
        "message": "your answer here"
    }
    """,

        input=messages
    )

    return json.loads(response.output_text)