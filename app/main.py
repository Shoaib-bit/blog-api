from fastapi import FastAPI
from routes.blog_route import router as blog_route
from models.blog_model import Blog
from database import engine, Base  

app = FastAPI()
Base.metadata.create_all(bind=engine) 

app.include_router(blog_route)
