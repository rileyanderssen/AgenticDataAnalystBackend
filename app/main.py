from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse 
from app.agents.orchestrator import Orchestrator
from app.models.schemas import UserFileDataRequest

app = FastAPI(title="Personal Data Analyst")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/api/health_check")
async def health_check():
    return {"message": "Hello from server"}

@app.post("/api/data_enquiry")
async def visualize_data(
    file: UploadFile = File(...),
    user_query: str = Form(""),
    requested_output_type: str = Form(""),
    chart_type: str = Form("")
):
    orchestrator = Orchestrator(
        file,
        user_query,
        requested_output_type,
        chart_type
    )

    response = await orchestrator.coordinate()
    if response is not None:
        return { 
            "answer": response 
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)