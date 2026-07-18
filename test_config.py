from app.core.config import get_settings

settings = get_settings()

print(settings.app_name)
print(settings.llm_model)
print(settings.chroma_db)