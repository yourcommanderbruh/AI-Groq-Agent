from agent.llm import call_llm
from agent.schema import AgentConfig
from agent.tools import TOOLS
from agent.memory import Memory


class Agent:
    def __init__(self, goal: str):
        self.goal = goal
        self.memory = Memory()

    def step(self):

        print("\n--- NEW STEP ---")

        prompt = f"""
Goal: {self.goal}

Memory:
{self.memory.context()}

What should I do next?
Respond in JSON.
"""

        raw_response = call_llm(prompt)

        try:
            action = AgentConfig(**raw_response)
        except Exception as e:
            print("Invalid response:", e)
            return True

        print("Thought:", action.thought)

        self.memory.add(f"Thought: {action.thought}")

        if action.action == "finish":
            print("Agent finished.")
            return False

        if action.action in TOOLS:

            try:
                result = TOOLS[action.action](**action.input)

                print("Tool result:", result)

                self.memory.add(f"Result: {result}")

            except Exception as e:

                print("Tool error:", e)

                self.memory.add(f"Error: {e}")

        else:

            print("Unknown tool:", action.action)

            self.memory.add("Unknown tool used.")

        return True