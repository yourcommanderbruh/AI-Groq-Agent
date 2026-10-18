class Memory:
    def __init__(self):
        self.events = []

    def add(self,event:str):
        self.events.append(event)

    def context(self,limit:int=5)->str:
        return "\n".join(self.events[-limit:])