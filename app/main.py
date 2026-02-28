from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="Tasks manager")

app.include_router(users.router)