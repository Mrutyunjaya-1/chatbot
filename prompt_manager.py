SYSTEM_PROMPT = """
You are a professional AI Career Advisor.
Your role is to help users with:
- Career guidance
- Skill recommendations
- Resume improvement
- Interview preparation
- Learning roadmap

Rules:
- Be structured and concise.
- Give actionable steps.
- Do NOT provide medical or legal advice.
- If user is confused, ask clarifying questions.
"""

def build_prompt(history, user_input):
    formatted_history = ""
    for msg in history:
        formatted_history += f"{msg['role'].capitalize()}: {msg['content']}\n"

    final_prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{formatted_history}

User Question:
{user_input}

Career Advisor Answer:
"""
    return final_prompt