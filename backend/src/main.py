from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from langchain_community.llms import Ollama
import os

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LLMInput(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Connected to FastAPI"}

@app.post("/download_model/{model}")
async def download_model(model):
    body = {
        "name": model,
    }
    response = requests.post(os.environ["OLLAMA_API_URL"] + "/api/pull", json=body)
    if response.ok:
        return "Pulled " + model
    else:
        return "Failed to pull model."

@app.post("/generate/")
async def llm_generate(input: LLMInput):
    llm = Ollama(model="mistral", base_url=os.environ["OLLAMA_API_URL"])

    return llm.invoke(input.message)