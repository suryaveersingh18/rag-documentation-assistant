import sys
from app.ingestion.ingest import IngestionPipeline

pipeline = IngestionPipeline()

# PDF
# pipeline.ingest("documents/python.pdf")

# Markdown
# pipeline.ingest("documents/readme.md")

# Website
pipeline.ingest("https://fastapi.tiangolo.com/")