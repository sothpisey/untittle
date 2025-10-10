from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from db.base import fetch_hashed_password
from security.authenticator import verify_password
from security.token_handler import create_access_token
from fastapi.responses import JSONResponse
from security.token_handler import get_current_user
from security.token_handler import oauth2_scheme

router = APIRouter(prefix='/api/auth', tags=['auth'])

class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Fetch user’s hashed password from DB
    hashed_password = fetch_hashed_password(form_data.username)
    if not hashed_password or not verify_password(form_data.password, hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get('/verify')
def verify_token(token: str = Depends(oauth2_scheme), username: str = Depends(get_current_user)):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={'message': 'Token is valid', 'username': username}
    )