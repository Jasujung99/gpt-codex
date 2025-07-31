from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .db import get_session

router = APIRouter(prefix="/projects", tags=["projects"])

@router.get("/")
async def list_projects(session: AsyncSession = Depends(get_session)):
    # Placeholder: fetch projects from the database
    return []

@router.post("/")
async def create_project(session: AsyncSession = Depends(get_session)):
    # Placeholder: create a new project
    return {"message": "project created"}
