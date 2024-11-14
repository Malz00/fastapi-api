from fastapi import FastAPI, Depends, status
from . import model
from .database import engine
from .routers import blogs, users, authentication

app = FastAPI()

model.Base.metadata.create_all(engine)


app.include_router(authentication.router)

app.include_router(blogs.router)

app.include_router(users.router)

