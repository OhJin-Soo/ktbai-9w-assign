from fastapi import APIRouter, Form, UploadFile, File
from Controllers.signin_controller import edit_profile

router = APIRouter()

@router.post("/edit")
async def edit_profile_route(
    image: UploadFile = File(None),
    email: str = Form(...),
    password: str = Form(...),
    password_confirm: str = Form(...),
    nickname: str = Form(...),
):
    return edit_profile(image, email, password, password_confirm, nickname)
