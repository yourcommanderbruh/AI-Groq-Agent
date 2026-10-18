🤖 Simple AI Agent From Scratch

Build a beginner-friendly AI agent from scratch using Python.
This project demonstrates how an agent can think, choose tools, execute actions, and update memory in a loop.

The goal of this project is to help you understand agentic AI architecture, not just call an LLM.

📚 What You'll Learn

This project shows how to build a simple AI agent that can:

Think about a goal

Decide which tool to use

Execute tools

Store results in memory

Repeat until the task is complete

You will learn the core architecture behind modern AI agents.

🧠 Agent Architecture
User Goal
   ↓
Agent Loop
   ↓
LLM decides next action
   ↓
Tool executes action
   ↓
Result stored in memory
   ↓
Agent continues or finishes

Agent Loop:

Think → Act → Observe → Remember → Repeat
🗂 Project Structure
agent-from-scratch/
│
├── agent/
│   ├── __init__.py
│   ├── agent.py       # Core agent loop
│   ├── llm.py         # LLM interface (Groq API)
│   ├── tools.py       # Agent tools (calculator + shell)
│   ├── memory.py      # Memory storage
│   └── schema.py      # Response validation
│
├── main.py            # Entry point
├── requirements.txt
└── .env
🛠 Tools Implemented
Calculator Tool

Allows the agent to perform math operations.

Example:

45 * 12

Result:

540
Run Shell Tool

Allows the agent to execute simple system commands.

Example:

ls

Output:

main.py
agent/
requirements.txt
⚙️ Requirements

Python 3.9+

Install dependencies:

pip install -r requirements.txt
🔑 Setup API Key

This project uses Groq LLM API.

Create a .env file:

GROQ_API_KEY=your_api_key_here
▶ Run the Agent

Start the agent with:

python main.py

Example output:

--- NEW STEP ---
Thought: I should calculate 45 * 12
Tool result: 540

--- NEW STEP ---
Thought: The answer is 540
Agent finished
📦 Dependencies
groq
pydantic
python-dotenv
🎯 Example Goals

Try changing the goal in main.py.

Example:

Calculate 25 * 18

or

List files in this directory

The agent will decide which tool to use.