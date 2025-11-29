from typing import List, Dict, Any
from app.LLM.prompt_gen import PromptGenerator
from app.LLM.communicator import Communictor

class PythonAgent:
    def __init__(
        self,
        headers: List[str],
        rows: List[Dict[str, Any]],
        user_query: str,
        chart_type: str
    ):
        self.headers = headers
        self.rows = rows
        self.user_query = user_query
        self.chart_type = chart_type

    async def determine_query_answer(self) -> str:
        prompt_generator = PromptGenerator(self.headers, self.rows, self.user_query)

        general_query_prompt = prompt_generator.generate_general_query()

        communicator = Communictor(general_query_prompt)
        answer = await communicator.send_prompt()

        return answer
        
    async def determine_chart_query_answer(self) -> str:
        prompt_generator = PromptGenerator(self.headers, self.rows, self.user_query)

        if self.chart_type == "Any":
            chart_query_prompt = prompt_generator.generate_chart_any_query()    
        else:
            chart_query_prompt = prompt_generator.generate_chart_query()

        communicator = Communictor(chart_query_prompt)

        # TODO -> create a code validator tool, loop until valid response
        answer = await communicator.send_prompt()
        print("== PRINTING ANSWER ===")
        print(answer)

        return answer


    