from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My FastAPI Application",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Allows one origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


