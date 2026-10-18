

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:
    from agent.agent import Agent
except ModuleNotFoundError as exc:
    if exc.name != "agent":
        raise
    from .agent.agent import Agent


def run_agent(goal: str):
    """
    Helper function to run an agent with a goal
    """

    print("\n==============================")
    print("Starting Agent")
    print("Goal:", goal)
    print("==============================")

    agent = Agent(goal=goal)

    running = True
    steps = 0
    max_steps = 5

    while running and steps < max_steps:
        running = agent.step()
        steps += 1

    print("\nAgent session finished.")
    print("==============================\n")


# Agent 1 → Calculator example
run_agent("Calculate 45 multiplied by 12")


# Agent 2 → Shell command example
run_agent("List all files in the current directory")