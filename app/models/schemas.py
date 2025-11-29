from pydantic import BaseModel
from typing import List, Dict, Any 

class FileData(BaseModel):
    file_type: str
    headers: List[str]
    rows: List[Dict[str, Any]]

class UserFileDataRequest(BaseModel):
    user_query: str = ""
    requested_output_type: str = ""
    chart_type: str = ""
