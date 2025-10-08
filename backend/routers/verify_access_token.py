from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from security.token_handler import get_current_user
from security.token_handler import oauth2_scheme

router = APIRouter(prefix='/api')

@router.get('/verify_token')
def verify_token(token: str = Depends(oauth2_scheme), username: str = Depends(get_current_user)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'message': 'Token is valid', 'username': username}
    )