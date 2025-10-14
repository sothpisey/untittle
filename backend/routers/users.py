from fastapi import APIRouter, Depends
from db.base import fetch_user_info, User
from security.token_handler import get_current_user
from fastapi.responses import JSONResponse

router = APIRouter(prefix='/api/v1/users', tags=['users'])

@router.get('/me', response_model=User)
def get_user_info(username: str = Depends(get_current_user)):
    user_info = fetch_user_info(username, is_username=True)
    if not user_info:
        return JSONResponse(
            status_code=404,
            content={'message': 'User not found'}
        )
    return user_info
