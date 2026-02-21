from google import genai
from backend.config import GEMINI_API_KEY
from backend.logger import logger

class GeminiClient:
    def __init__(self, model_name="models/gemini-flash-latest"):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            return response.text
        except Exception as e:
            print("GEMINI ERROR:", e)
            logger.error(f"Gemini API Error: {str(e)}")
            return "⚠️ Sorry, I'm facing a technical issue right now. Please try again."