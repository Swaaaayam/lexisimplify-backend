from fastapi import APIRouter
from pydantic import BaseModel
from utils.llm_helper import simplify_text

router = APIRouter()

class SimplifyRequest(BaseModel):
    clause: str

@router.post("/")
async def simplify(req: SimplifyRequest):
    simplified = simplify_text(req.clause)
    return {"simplified": simplified}
