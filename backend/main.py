a
from fastapi import FastAPI

app = FastAPI(
    title="Atlas Search API",
    description="A local web search engine.",
    version="0.1.0",
)


@app.get("/api/v1/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Atlas Search",
    }
