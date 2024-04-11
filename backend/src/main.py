from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from langchain_community.llms import Ollama
import time
import subprocess
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

def pull_ollama_model(model_name: str):
    result = subprocess.run(["ollama", "pull", model_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Model {model_name} pulled successfully")
    else:
        print(f"Failed to pull model {model_name}: {result.stderr}")

@app.on_event("startup")
async def startup_event():

    for _ in range(10):
        try:
            response = requests.get(os.environ["OLLAMA_API_URL"])
            if response.ok:
                break
        except requests.exceptions.ConnectionError:
            time.sleep(3)
    else:
        raise Exception("Ollama service is not ready")
    # Using subprocess to run the shell command
    result = subprocess.run(["ollama", "pull", "mistral"], capture_output=True, text=True)
    if result.returncode == 0:
        print("Model pulled successfully")
    else:
        print("Failed to pull model:", result.stderr)
        pull_ollama_model("mistral")        

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