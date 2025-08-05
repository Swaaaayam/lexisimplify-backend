from fastapi import APIRouter
from pydantic import BaseModel
from utils.llm_helper import answer_question

router = APIRouter()

class AskRequest(BaseModel):
    question: str
    context: str = ""

@router.post("/ask/")
async def ask(request: AskRequest):
    answer = answer_question(request.question, request.context)
    return {"answer": answer}
