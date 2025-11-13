from fastapi import HTTPException, UploadFile
from pathlib import Path
import shutil
from Models.editpost_model import PostModel

UPLOAD_DIR = Path("uploaded_images")
UPLOAD_DIR.mkdir(exist_ok=True)

class PostController:
    
    @staticmethod
    def validate_title(title: str):
        if len(title) > 26:
            raise HTTPException(status_code=400, detail="제목은 26자 이하로 작성해야 합니다.")
        return title

    @staticmethod
    async def save_image(file: UploadFile) -> str:
        if not file:
            return None
        if file.content_type not in ["image/png", "image/jpeg", "image/jpg", "image/gif"]:
            raise HTTPException(status_code=400, detail="이미지 파일만 업로드 가능합니다.")
        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
        return str(file_path)

    @staticmethod
    def build_post_response(file_name, title, content, image_url, version, created_at):
        return PostModel(
            file_name=file_name,
            title=title,
            content=content,
            image_url=image_url,
            version=version,
            created_at=created_at
        )
