from fastapi import UploadFile, File
import pandas as pd
from io import BytesIO
from app.models.schemas import FileData

"""
    Tool -> Extract data from csv or excel files

    Extract headers and data corresponding to each header
"""

class DataLoader:
    def __init__(self):
        pass

    async def process_file(self, file: UploadFile) -> FileData:
        """
        Determine file type and process data
        """

        file_type: str = self._determineFileType(file)

        if file_type == "" or file_type == "UNSUPPORTED":
            return FileData(
                file_type="Unsupported",
                headers=[],
                rows=[]
            )
        elif file_type == "ERROR":
            return FileData(
                file_type="Network error",
                headers=[],
                rows = []
            )
        
        contents = await file.read()

        if file_type == "Excel":
            df = pd.read_excel(BytesIO(contents))
        elif file_type == "CSV":
            df = pd.read_csv(BytesIO(contents))
        
        headers = df.columns.tolist()
        rows = df.to_dict(orient="records")

        return FileData(
            file_type=file_type,
            headers=headers,
            rows=rows,
            dataframe=df
        )


    def _determineFileType(self, file: UploadFile = File(...)) -> str:
        """
        Determine the file type
        """

        if file is None:
            return ""

        filename = file.filename.lower()
        
        try:
            if filename.endswith((".xls", ".xlsx")):
                return "Excel"
            elif filename.endswith(".csv"):
                return "CSV"
            else:
                return "UNSUPPORTED"
        except Exception as e:
            print(f"Error processing file: {e}")
            return "ERROR"