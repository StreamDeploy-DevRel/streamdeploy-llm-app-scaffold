from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from langchain_community.llms import Ollama
import os
from pymongo import MongoClient

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mongo_client = MongoClient(os.environ["MONGODB_ATLAS_URI"])
db = mongo_client.your_database_name
chat_history_collection = db.chat_history

class LLMInput(BaseModel):
    message: str
    answer: str

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

@app.post("/save_history/")
async def save_history(input: LLMInput):
    chat_history_collection.insert_one({"message": input.message, "answer": input.answer})
    return {"status": "History saved"}

@app.get("/get_history/")
def get_history():
    history = list(chat_history_collection.find({}, {'_id': 0}))
    return history