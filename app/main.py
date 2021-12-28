from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote

# Database Creation
# models.Base.metadata.create_all(bind=engine)

# FastAPI Instance Creation
app = FastAPI()

# Routes
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)
