from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import traceback

from app.graph import run_agent


app = FastAPI(
    title="Supply Chain GenAI Agent",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class ChatRequest(BaseModel):
    question: str



class ChatResponse(BaseModel):
    question: str
    answer: str



@app.get("/")
def home():

    return {
        "status": "running",
        "service": "Supply Chain AI Agent"
    }



@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:

        print("=" * 60)
        print("Question:", request.question)


        answer = run_agent(
            request.question
        )


        print("Answer:", answer)
        print("=" * 60)



        return ChatResponse(
            question=request.question,
            answer=answer
        )


    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )