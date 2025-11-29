import openai
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class Communictor:
    def __init__(self, prompt: str):
        self.prompt = prompt
    
    async def send_prompt(self):
        client = OpenAI(api_key=api_key)

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a data analyst assistant. Analyze the provided data and answer questions accurately."
                    },
                    {
                        "role": "user",
                        "content": self.prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )

            return response.choices[0].message.content
        
        except Exception as e:
            print("Failed to talk to LLM")
            return f"Error: {str(e)}"

