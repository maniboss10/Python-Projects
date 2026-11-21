
from fastapi import FastAPI
from backend.routers.health import router as health_router

app = FastAPI(
    title="Hybrid RAG API",
    description="Backend API for FAISS and Neo4j Hybrid RAG",
    version="0.1.0"
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Hybrid RAG API"
    }
