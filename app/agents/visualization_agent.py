from typing import Any
from app.tools.code_tool import CodeTool
import pandas as pd
import numpy as np

class VisualizationAgent:
    def __init__(
        self,
        df: Any,
        chart_type: str,
        aggregation_code: str
    ):
        self.df = df
        self.chart_type = chart_type
        self.aggregation_code = aggregation_code


    async def construct_chart(self):
        code_tool = CodeTool()

        if self.chart_type == "Any":
            components = self.aggregation_code.split('@')
            self.chart_type = components[1]
            self.aggregation_code = components[0]

        print("HELLO")
        pandas_result = await code_tool.execute_pandas_code(self.aggregation_code, self.df)
        normalized_result = self._normalize_for_chart(pandas_result)
        chart_config = self._create_chart_config(normalized_result)

        return chart_config

    def _normalize_for_chart(self, result) -> dict:
        # for type series
        if isinstance(result, pd.Series):
            return {
                'labels': result.index.tolist(),
                'values': result.values.tolist(),
                'type': 'series',
                'name': result.name or 'value'
            }
        
        elif isinstance(result, pd.DataFrame):
            if not isinstance(result.index, pd.RangeIndex):
                result = result.reset_index()

            if len(result.columns) == 2:
                labels = result.iloc[:, 0].astype(str).tolist()

                return {
                    'labels': labels,
                    'values': result.iloc[:, 1].tolist(),
                    'type': 'dataframe',
                    'columns': result.columns.tolist()
                }
            elif len(result.columns) > 2:
                labels = result.iloc[:, 0].astype(str).tolist()

                datasets = []
                for col in result.columns[1:]:
                    datasets.append({
                        'label': col,
                        'data': result[col].tolist()
                    })

                return {
                    'labels': labels,
                    'datasets': datasets,
                    'type': 'dataframe_multi_series',
                    'columns': result.columns.tolist()
                }
            else:
                return {
                    'data': result.to_dict('records'),
                    'columns': result.columns.tolist(),
                    'type': 'dataframe_result'
                }
        
        elif isinstance(result, pd.Index):
            return {
                'values': result.tolist(),
                'type': 'index'
            }
    
        elif isinstance(result, np.ndarray):
            return {
                'values': result.tolist(),
                'type': 'array'
            }

        elif isinstance(result, list):
            return {
                'values': result,
                'type': 'list'
            }
    
        elif isinstance(result, dict):
            return {
                'values': result,
                'type': 'dict'
            }
        
        else:
            return {
                'error': f'Cannot chart result type: {type(result).__name__}',
                'type': 'error',
                'raw': str(result)
            }
        
    def _create_chart_config(self, data: dict) -> dict:
        if data['type'] == 'series':
            labels = data['labels']
            values = data['values']
            data_name = data['name']
        elif data['type'] == 'dataframe':
            labels = data['labels']
            values = data['values']
            data_name = data['columns'][1]
        elif data['type'] == 'dataframe_multi_series':
            labels = data['labels']
            datasets = data['datasets']

            return self._create_multi_series_chart(labels, datasets)
        elif data['type'] == 'scalar':
            return {
                'type': 'metric',
                'value': data['value'],
                'error': 'Cannot create chart from single value'
            }
        else:
            return { 'error': f"Cannot chart type: {data['type']}" }
        
        if self.chart_type == 'Bar':
            return {
                'type': 'bar',
                'data': {
                    'labels': labels,
                    'datasets': [{
                        'label': data_name,
                        'data': values,
                        'backgroundColor': 'rgba(102, 126, 234, 0.8)',
                        'borderColor': 'rgba(102, 126, 234, 1)',
                        'borderWidth': 1
                    }]
                },
                'options': {
                    'responsive': True,
                    'plugins': {
                        'title': {
                            'display': True,
                            'text': f'{data_name} by Category'
                        },
                        'legend': {
                            'display': False
                        }
                    },
                    'scales': {
                        'y': {
                            'beginAtZero': True
                        }
                    }
                }
            }
        elif self.chart_type == 'Line':
            return {
                'type': 'line',
                'data': {
                    'labels': labels,
                    'datasets': [{
                        'label': data_name,
                        'data': values,
                        'borderColor': 'rgba(102, 126, 234, 1)',
                        'backgroundColor': 'rgba(102, 126, 234, 0.1)',
                        'fill': True,
                        'tension': 0.4  # Smooth curve
                    }]
                },
                'options': {
                    'responsive': True,
                    'plugins': {
                        'title': {
                            'display': True,
                            'text': f'{data_name} Trend'
                        }
                    },
                    'scales': {
                        'y': {
                            'beginAtZero': True
                        }
                    }
                }
            }
        elif self.chart_type == 'Pie':
            return {
                'type': 'pie',
                'data': {
                    'labels': labels,
                    'datasets': [{
                        'label': data_name,
                        'data': values,
                        'backgroundColor': [
                            'rgba(255, 99, 132, 0.8)',
                            'rgba(54, 162, 235, 0.8)',
                            'rgba(255, 206, 86, 0.8)',
                            'rgba(75, 192, 192, 0.8)',
                            'rgba(153, 102, 255, 0.8)',
                            'rgba(255, 159, 64, 0.8)',
                            'rgba(199, 199, 199, 0.8)',
                            'rgba(83, 102, 255, 0.8)',
                            'rgba(255, 99, 255, 0.8)',
                            'rgba(99, 255, 132, 0.8)',
                        ],
                        'borderWidth': 2
                    }]
                },
                'options': {
                    'responsive': True,
                    'plugins': {
                        'title': {
                            'display': True,
                            'text': f'{data_name} Distribution'
                        },
                        'legend': {
                            'position': 'right'
                        }
                    }
                }
            }
        
        else:
            return {'error': f'Unsupported chart type: {self.chart_type}'}

    def _create_multi_series_chart(self, labels: list, datasets: list) -> dict:
        colors = [
            'rgba(255, 99, 132, 0.8)',
            'rgba(54, 162, 235, 0.8)',
            'rgba(255, 206, 86, 0.8)',
            'rgba(75, 192, 192, 0.8)',
            'rgba(153, 102, 255, 0.8)',
            'rgba(255, 159, 64, 0.8)',
        ]
        
        for i, dataset in enumerate(datasets):
            dataset['backgroundColor'] = colors[i % len(colors)]
            dataset['borderColor'] = colors[i % len(colors)].replace('0.8', '1')
            dataset['borderWidth'] = 2
            if self.chart_type == 'Line':
                dataset['fill'] = False
                dataset['tension'] = 0.6
            
        if self.chart_type == 'Bar':
            return {
                'type': 'bar',
                'data': {
                    'labels': labels,
                    'datasets': datasets
                },
                'options': {
                    'responsive': True,
                    'plugins': {
                        'title': {
                            'display': True,
                            'text': 'Sales by Product Over Time'
                        },
                        'legend': {
                            'display': True,
                            'position': 'top'
                        }
                    },
                    'scales': {
                        'x': {'stacked': True},  
                        'y': {'stacked': True, 'beginAtZero': True}
                    }
                }
            }
        
        elif self.chart_type == 'Line':
            return {
                'type': 'line',
                'data': {
                    'labels': labels,
                    'datasets': datasets
                },
                'options': {
                    'responsive': True,
                    'plugins': {
                        'title': {
                            'display': True,
                            'text': 'Sales Trends by Product'
                        },
                        'legend': {
                            'display': True,
                            'position': 'top'
                        }
                    },
                    'scales': {
                        'y': {'beginAtZero': True}
                    }
                }
            }
        
        else:
            return {'error': 'Multi-series only supports Bar and Line charts'}