from typing import List, Dict, Any

class PromptGenerator:
    def __init__(
        self,
        headers: List[str],
        rows: List[Dict[str, Any]],
        user_query: str
    ):
        self.headers = headers
        self.rows = rows
        self.user_query = user_query
    
    # For multi-level queries making use of more than two columns, use group by with unstack().
    def generate_chart_query(self) -> str:
        header_data = self._format_header_data()

        prompt = f"""
        You are an expert data analyst.

        The user provided this query: {self.user_query}

        The CSV/Excel schema provided for this query is: {header_data}

        Return ONLY pandas aggregation code so that a graph can be made (do not include reset_index()).
        EXAMPLE OF EXPECTED RESPONSE: df.groupby('Product')['Sales'].sum()
        """

        return prompt
    
    def generate_chart_any_query(self) -> str:
        header_data = self._format_header_data()

        prompt = f"""
        You are an expert data analyst.

        The user provided this query: {self.user_query}

        The CSV/Excel schema provided for this query is: {header_data}

        Please also select the best chart option for this data out of either:
        'Pie',
        'Line',
        'Bar'

        Append the chart type at the end of the aggregated code prefixed by '@'

        Return ONLY pandas aggregation code so that a graph can be made.
        EXAMPLE OF EXPECTED RESPONSE: df.groupby('Product')['Sales'].sum()@Bar
        """

        return prompt

    def generate_general_query(self) -> str:
        header_data = self._format_header_data()
        row_data = self._format_row_data()

        prompt = f"""
        You are an expert data analyst.

        The user as provide this query: {self.user_query}

        The data provided for this query is detailed below.
        Headers: {header_data}
        Row Data: {row_data}

        Return only a breif paragraph answering the query. Do not add any personal
        text before or after, your response must only contain the answer to the query.
        """

        return prompt


    def _format_header_data(self) -> str:
        return ", ".join(self.headers)
    
    def _format_row_data(self) -> str:
        row_data = ""
        for i, row in enumerate(self.rows, 1):
            row_values = [str(row.get(header, "")) for header in self.headers]
            row_data += f"Row {i}: {', '.join(row_values)}\n"
        
        return row_data