from pydantic import BaseModel, constr
from typing import Optional

class PostModel(BaseModel):
    file_name: str
    title: constr(max_length=26)  # 제목 최대 26자
    content: str
    image_url: Optional[str] = None
    version: str
    created_at: str

