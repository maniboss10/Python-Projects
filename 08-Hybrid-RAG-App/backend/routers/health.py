
from fastapi import APIRouter

router = APIRouter(
    prefix="/api",
    tags=["Health"]
)


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "hybrid-rag-backend",
        "version": "0.1.0"
    }
