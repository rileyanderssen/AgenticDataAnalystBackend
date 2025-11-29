🧠 Agentic Data Analyst (Python Backend)

The Agentic Data Analyst is a backend service that allows users to upload structured data files (CSV/Excel) and interact with them conversationally.
Users can ask natural-language questions, explore insights, and generate visualizations — all powered by a Python analysis engine.

🚀 Features

📄 File Upload
- Upload CSV or Excel files
- Automatic data validation and cleaning
- In-memory or temporary storage for analysis

🤖 Natural-Language Data Queries
Ask questions like:
- “What is the average sales by region?”
- “Show me the distribution of ages.”
- “Which columns have missing values?”
The system interprets queries and executes the necessary Python/Pandas code behind the scenes.

📊 Data Visualization
Generate high-quality plots using Matplotlib, Seaborn, or Plotly:
- Bar charts
- Line charts
- Histograms
- Scatter plots
- Heatmaps
The backend returns either an image or a JSON-encoded graphic representation.

🔎 Intelligent Data Understanding
- Automatic inference of column types
- Summaries, correlations, outliers
- Context-aware suggestions (e.g., recommended visualizations)

🧰 Tech Stack
- Python 3.10+
- FastAPI
- Pandas for data handling
- OpenAI API for natural language interpretation
- React (Vite) for web GUI
