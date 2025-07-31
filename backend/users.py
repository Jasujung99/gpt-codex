from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_session

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def list_users(session: AsyncSession = Depends(get_session)):
    # Placeholder: fetch users from the database
    return []

@router.post("/")
async def create_user(session: AsyncSession = Depends(get_session)):
    # Placeholder: create a new user
    return {"message": "user created"}
