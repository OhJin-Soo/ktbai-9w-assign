from typing import List
from pathlib import Path
from fastapi import UploadFile
from models.post_model import PostCreate, PostResponse

UPLOAD_DIR = Path("uploaded_images")
UPLOAD_DIR.mkdir(exist_ok=True)

posts: List[PostResponse] = []
post_id_counter = 1

def create_post(post_data: PostCreate, image: UploadFile = None) -> PostResponse:
    global post_id_counter

    image_filename = None
    if image:
        image_filename = f"{post_id_counter}_{image.filename}"
        with open(UPLOAD_DIR / image_filename, "wb") as f:
            f.write(image.file.read())

    post = PostResponse(
        id=post_id_counter,
        title=post_data.title,
        content=post_data.content,
        image_filename=image_filename
    )

    posts.append(post)
    post_id_counter += 1
    return post

def list_posts() -> List[PostResponse]:
    return posts
