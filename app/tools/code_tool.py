import pandas as pd
from typing import Any
import numpy as np

class CodeTool:
    def __init__(self):
        pass

    async def execute_pandas_code(self, code: str, df: pd.DataFrame) -> Any:
        df = self._convert_date_columns(df)
        
        if 'result =' not in code:
            code = f"result = {code}"

        namespace = {
            'pd': pd,
            'df': df,
            'np': np,
            'result': None
        }

        exec(code, namespace)

        return namespace['result']
    
    def _convert_date_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        for col in df.columns:
            if 'date' in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass  
        
        return df