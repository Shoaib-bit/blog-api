from fastapi import FastAPI
from routes.blog_route import router as blog_route

app = FastAPI()

app.include_router(blog_route)


