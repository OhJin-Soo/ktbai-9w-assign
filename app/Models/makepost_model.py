from pydantic import BaseModel, constr
from typing import Optional

class PostCreate(BaseModel):
    title: constr(max_length=26)
    content: str
    image_filename: Optional[str] = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    image_filename: Optional[str] = None
