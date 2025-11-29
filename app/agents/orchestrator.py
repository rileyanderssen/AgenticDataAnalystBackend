from typing import Optional, Any
from fastapi import UploadFile, File
from app.tools.data_loader import DataLoader
from app.agents.python_agent import PythonAgent

class Orchestrator:
    def __init__(
            self,
            file: UploadFile = File(...),
            user_query: str = "",
            requested_output_type: str = "",
            chart_type: str = ""
        ):

        self.data_loader = DataLoader()
        self.file = file
        self.user_query = user_query
        self.requested_output_type = requested_output_type
        self.chart_type = chart_type

    async def coordinate(self) -> Any:
        if self.file is None:
            return
        
        file_data = await self.data_loader.process_file(self.file)

        if self.requested_output_type == "general enquiry":
            python_agent = PythonAgent(file_data.headers, file_data.rows, self.user_query)

            answer = await python_agent.determine_query_answer()

            return answer


    

