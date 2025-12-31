from fastapi import FastAPI
from src.api.users import router as user_router

app = FastAPI(title="Clothing User Service")

app.include_router(user_router, prefix="/users", tags=["Users"])

@app.get("/health")
def health():
    return {"status": "UP"}
