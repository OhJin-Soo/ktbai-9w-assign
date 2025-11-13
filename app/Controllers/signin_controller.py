import re

def edit_profile(image, email, password, password_confirm, nickname):
    # 1️⃣ 프로필 이미지 유효성 검사
    if image:
        filename = image.filename.lower()
        if not filename.endswith((".png", ".jpg", ".jpeg", ".gif")):
            return {"success": False, "message": "이미지 파일만 업로드 가능합니다."}
    else:
        filename = None  # 이미지 미업로드 허용

    # 2️⃣ 이메일 형식 검사
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return {"success": False, "message": "유효하지 않은 이메일 형식입니다."}

    # 중복 이메일 예시 검증 (DB 없음 → mock)
    existing_emails = ["example@developia.com", "test@developia.com"]
    if email in existing_emails:
        return {"success": False, "message": "이미 등록된 이메일입니다."}

    # 3️⃣ 비밀번호 유효성 검사
    if not password:
        return {"success": False, "message": "비밀번호를 입력해주세요"}
    if len(password) < 8 or len(password) > 20:
        return {"success": False, "message": "비밀번호 형식을 확인해주세요 (8~20자)"}
    if not re.search(r"[A-Z]", password):
        return {"success": False, "message": "비밀번호 형식을 확인해주세요 (대문자 포함)"}
    if not re.search(r"[a-z]", password):
        return {"success": False, "message": "비밀번호 형식을 확인해주세요 (소문자 포함)"}
    if not re.search(r"\d", password):
        return {"success": False, "message": "비밀번호 형식을 확인해주세요 (숫자 포함)"}
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return {"success": False, "message": "비밀번호 형식을 확인해주세요 (특수문자 포함)"}

    # 4️⃣ 비밀번호 확인
    if not password_confirm:
        return {"success": False, "message": "비밀번호를 한번 더 입력해주세요"}
    if password != password_confirm:
        return {"success": False, "message": "비밀번호 확인과 다릅니다"}

    # 5️⃣ 닉네임 검사
    if len(nickname) < 2 or len(nickname) > 10:
        return {"success": False, "message": "닉네임 형식을 확인해주세요 (2~10자)"}
    if not re.match(r"^[가-힣a-zA-Z0-9]+$", nickname):
        return {"success": False, "message": "닉네임 형식을 확인해주세요 (한글, 영어, 숫자만 가능)"}

    # ✅ 모든 조건 통과
    return {
        "success": True,
        "message": "회원정보 수정이 완료되었습니다.",
        "data": {
            "email": email,
            "nickname": nickname,
            "image_filename": filename,
        },
    }
