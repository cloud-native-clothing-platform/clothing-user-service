from fastapi import APIRouter
from src.models.schemas import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return UserResponse(
        user_id="USR-001",
        name=user.name,
        email=user.email,
        status="ACTIVE"
    )

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: str):
    return UserResponse(
        user_id=user_id,
        name="Demo User",
        email="demo@clothing.com",
        status="ACTIVE"
    )
