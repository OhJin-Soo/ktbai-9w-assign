from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=20)
    password_confirm: str
    nickname: str = Field(..., min_length=1, max_length=10)
    profile_image: Optional[str] = None  # 이미지 URL 또는 경로
