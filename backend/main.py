from fastapi import FastAPI, Depends
from db.base import fetch_all
from routers import auth, users, products
from security.token_handler import get_current_user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    docs_url='/api/docs',
    redoc_url='/api/redoc',
    openapi_url='/api/openapi.json'
)

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://47.84.64.277',
        '*'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)