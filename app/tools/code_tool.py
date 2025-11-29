import pandas as pd
from typing import Any
import numpy as np

class CodeTool:
    def __init__(self):
        pass

    async def execute_pandas_code(self, code: str, df: pd.DataFrame) -> Any:
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