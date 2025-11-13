from fastapi import APIRouter, Form, File, UploadFile
from fastapi.responses import JSONResponse
from Controllers.editpost_controller import PostController

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/edit")
async def edit_post(
    file_name: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    version: str = Form(...),
    created_at: str = Form(...),
    image: UploadFile = File(None)
):
    # 제목 검증
    PostController.validate_title(title)

    # 이미지 저장
    image_url = await PostController.save_image(image)

    # JSON 응답 생성
    post = PostController.build_post_response(
        file_name=file_name,
        title=title,
        content=content,
        image_url=image_url,
        version=version,
        created_at=created_at
    )

    return JSONResponse(content=post.dict())
