<p align="center">
  <h1 align="center">🧠 Agentic Data Analyst</h1>
  <p align="center">
    A conversational backend service for intelligent data analysis
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/framework-FastAPI-009688.svg" alt="FastAPI">
  <img src="https://img.shields.io/badge/AI-OpenAI-412991.svg" alt="OpenAI">
</p>

---

## 📖 Overview

The **Agentic Data Analyst** transforms how you interact with structured data. Upload CSV or Excel files and ask questions in plain English — no SQL or Python knowledge required. The system automatically interprets your queries, performs sophisticated analysis, and generates beautiful visualizations.

Perfect for data scientists, analysts, and business users who want quick insights without writing code.

---

## ✨ Features

### 📄 **File Upload & Processing**
- Support for CSV and Excel formats
- Automatic data validation and cleaning
- Efficient in-memory storage for fast analysis

### 💬 **Natural Language Queries**
Ask questions conversationally:
- *"What is the average sales by region?"*
- *"Show me the distribution of ages"*
- *"Which columns have missing values?"*

The engine interprets your intent and executes the appropriate Pandas operations automatically.

### 📊 **Dynamic Visualizations**
Generate professional charts with zero configuration:
- Bar charts and line graphs
- Histograms and scatter plots
- Correlation heatmaps
- Distribution analysis

Powered by Matplotlib, Seaborn, and Plotly for publication-quality graphics.

### 🔍 **Intelligent Data Understanding**
- Automatic column type inference
- Statistical summaries and correlations
- Outlier detection
- Smart visualization recommendations based on data characteristics

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.10+ |
| **API Framework** | FastAPI |
| **Data Processing** | Pandas |
| **AI Engine** | OpenAI API |
| **Frontend** | React (Vite) |
| **Visualization** | Matplotlib, Seaborn, Plotly |

---

## 🚀 Getting Started
```bash
# Clone the repository
git clone https://github.com/yourusername/agentic-data-analyst.git

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your OpenAI API key to .env

# Run the server
uvicorn main:app --reload
```

---

## 📦 Installation

**Requirements:**
- Python 3.10 or higher
- OpenAI API key
- Node.js (for frontend)

**Python Dependencies:**
```bash
pip install fastapi uvicorn pandas openpyxl matplotlib seaborn plotly openai
```

---

## 💡 Usage Example
```python
# Upload a file
POST /upload
Content-Type: multipart/form-data

# Ask a question
POST /query
{
  "question": "What are the top 5 products by revenue?",
  "file_id": "abc123"
}

# Generate visualization
POST /visualize
{
  "query": "Show sales trends over time",
  "chart_type": "line",
  "file_id": "abc123"
}
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

Built with ❤️ using modern Python and AI technologies.

---

<p align="center">
  Made with 🧠 and ☕
</p>