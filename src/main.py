from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.recommend.router import router as recommend_router

app = FastAPI()

origins = ["http://localhost:8888"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommend_router)
