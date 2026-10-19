"""Minimal user profile API; authentication belongs at the platform edge."""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI(title="Clothing User Service", version="1.0.0")
class UserCreate(BaseModel):
    id: str = Field(min_length=3, max_length=64)
    name: str = Field(min_length=1, max_length=100)
    email: str
class User(UserCreate):
    active: bool = True
USERS: dict[str, User] = {}
@app.get("/health")
def health(): return {"status": "ok", "service": "user"}
@app.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    if user.id in USERS: raise HTTPException(409, "User ID already exists")
    result = User(**user.model_dump())
    USERS[user.id] = result
    return result
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: str):
    if user_id not in USERS: raise HTTPException(404, "User not found")
    return USERS[user_id]
