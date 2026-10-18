from pydantic import BaseModel
from typing import Dict, Any

class AgentConfig(BaseModel):
    thought:str
    action:str
    input:Dict[str, Any]