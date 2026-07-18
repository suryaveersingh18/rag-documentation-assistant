from fastapi import APIRouter

from app.api.schemas import ChatRequest
from app.api.schemas import ChatResponse
from app.api.schemas import IngestRequest
from app.graph.workflow import graph
from app.ingestion.ingest import IngestionPipeline

router = APIRouter()

pipeline = IngestionPipeline()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = graph.invoke(
        {
            "question": request.question
        }
    )

    sources = []

    for doc in result["documents"]:
        source = doc.metadata.get("source")

        if source and source not in sources:
            sources.append(source)

    return ChatResponse(
        answer=result["answer"],
        sources=sources,
    )


@router.post("/ingest")
def ingest(request: IngestRequest):

    try:
        pipeline.ingest(request.source)

        return {
            "message": "Document ingested successfully."
        }

    except Exception as e:
        from fastapi import HTTPException

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )