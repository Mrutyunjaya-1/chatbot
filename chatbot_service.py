from backend.gemini_client import GeminiClient
from backend.prompt_manager import build_prompt
from backend.memory import ConversationMemory

class ChatbotService:
    def __init__(self):
        self.client = GeminiClient()
        self.memory = ConversationMemory()

    def get_response(self, user_input):
        history = self.memory.get_recent()
        prompt = build_prompt(history, user_input)

        response = self.client.generate(prompt)

        self.memory.add("user", user_input)
        self.memory.add("assistant", response)

        return response