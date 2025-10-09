from fastapi import APIRouter, Depends
from db.base import fetch_user_info
from security.token_handler import get_current_user
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/api')

@router.get("/user_info")
def get_user_info(username: str = Depends(get_current_user)):
    user_info = fetch_user_info(username, is_username=True)
    if user_info:
        user_info = {k: v for k, v in user_info.__dict__.items() if not k.startswith("_")}
        return JSONResponse(content=user_info)
    return JSONResponse(content={"error": "User not found"}, status_code=404)
