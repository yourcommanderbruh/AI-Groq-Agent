import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


SYSTEM_PROMPT = """
You are an autonomous AI agent.

You must ALWAYS respond in JSON format.

JSON structure:

{
  "thought": "explain your reasoning",
  "action": "tool name or finish",
  "input": {}
}

Available tools:

1. calculator
Description: evaluate a mathematical expression.

Input format:
{
  "expression": "math expression"
}

Example:
{
  "thought": "I should calculate 45 multiplied by 12",
  "action": "calculator",
  "input": {
    "expression": "45 * 12"
  }
}


2. run_shell
Description: execute a shell command.

Input format:
{
  "command": "shell command"
}

Example:
{
  "thought": "I should list files in the directory",
  "action": "run_shell",
  "input": {
    "command": "ls"
  }
}


Rules:
- action must be one of: calculator, run_shell, finish
- never invent tool names
- always return valid JSON
"""


def call_llm(prompt: str) -> dict:

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    # Convert JSON string → Python dictionary
    return json.loads(content)