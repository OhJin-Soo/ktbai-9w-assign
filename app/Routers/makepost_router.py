from fastapi import APIRouter, Form, UploadFile, File, HTTPException
from typing import List
from Controllers.makepost_controller import create_post, list_posts
from models.makepost_model import PostCreate, PostResponse

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/", response_model=PostResponse)
async def add_post(
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None)
):
    if not title or len(title) > 26:
        raise HTTPException(status_code=400, detail="Title must be 1-26 characters.")
    if not content:
        raise HTTPException(status_code=400, detail="Content cannot be empty.")

    post_data = PostCreate(title=title, content=content)
    return create_post(post_data, image)

@router.get("/", response_model=List[PostResponse])
async def get_posts():
    return list_posts()
