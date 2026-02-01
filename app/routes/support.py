from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field
from app.services.prompt_service import build_prompt
from app.services.ai_service import generate_ai_response
from app.utils.logger import logger
from app.utils.security import rate_limiter

router = APIRouter(prefix="/support", tags=["Support"])

class SupportRequest(BaseModel):
    query: str = Field(..., min_length=5)

class SupportResponse(BaseModel):
    response: str

@router.post("/", response_model=SupportResponse)
def get_support(req: SupportRequest, request: Request):
    try:
        client_ip = request.client.host
        rate_limiter(client_ip)

        logger.info(f"Support query received from {client_ip}: {req.query}")

        prompt = build_prompt(req.query)
        ai_reply = generate_ai_response(prompt)

        return {"response": ai_reply}

    except HTTPException:
        raise

    except Exception as e:
        logger.error(f"Support processing failed: {e}")
        raise HTTPException(
            status_code=500,
            detail="Internal server error. Please try again later."
        )
