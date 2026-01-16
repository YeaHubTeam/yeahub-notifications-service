from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI()

# Весь API под /v1
app.include_router(api_router, prefix="/v1")
