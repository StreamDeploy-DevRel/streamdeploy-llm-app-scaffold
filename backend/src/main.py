from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import Ollama

app = FastAPI()

class LLMInput(BaseModel):
    message: str


@app.get("/")
def read_root():
    return {"message": "Connected to FastAPI"}

@app.post("/generate/")
async def llm_generate(input: LLMInput):
    llm = Ollama(model="mistral")

    return llm.invoke(input.message)