class ConversationMemory:
    def __init__(self):
        self.history = []

    def add(self, role, message):
        self.history.append({"role": role, "content": message})

    def get_recent(self, limit=6):
        return self.history[-limit:]