from typing import Optional, Any
from fastapi import UploadFile, File
from app.tools.data_loader import DataLoader
from app.agents.python_agent import PythonAgent
from app.agents.visualization_agent import VisualizationAgent

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
            python_agent = PythonAgent(file_data.headers, file_data.rows, self.user_query, self.chart_type)

            answer = await python_agent.determine_query_answer()

            return answer
        else:
            python_agent = PythonAgent(file_data.headers, file_data.rows, self.user_query, self.chart_type)

            answer = await python_agent.determine_chart_query_answer()

            visualization_agent = VisualizationAgent(file_data.dataframe, self.chart_type, answer)
            chart_config = await visualization_agent.construct_chart()

            return chart_config



    

