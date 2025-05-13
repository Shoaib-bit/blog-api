
from sqlalchemy import or_
from typing import Optional
from fastapi import APIRouter, Depends, HTTPException
from database import get_db
from schema import Blog as Blog_Scheme
from sqlalchemy.orm import Session
from models.blog_model import Blog


router = APIRouter(
    tags = ["Blogs"],
    prefix='/blogs'
)

@router.get("/")
def get_blogs(search : Optional[str] = '', limit : Optional[int] = 10, page : Optional[int] = 1, db : Session = Depends(get_db)):
    offset = (page - 1) * limit

    query = db.query(Blog)

    if search:
        query = query.filter(
            or_(
                Blog.title.ilike(f'%{search}%'),  
                Blog.content.ilike(f'%{search}%')  
            )
        )

    blogs = query.order_by(Blog.id).limit(limit).offset(offset).all()

    return {
        "data" : blogs
    }


@router.post("/")
def create(request : Blog_Scheme,  db : Session = Depends(get_db)):
    new_blog = Blog(title = request.title, content = request.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return {
        "data" : new_blog
    }


@router.delete("/{id}")
def delete_blog(id : int, db : Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()

    if blog is None:
        return HTTPException(status_code=404, detail="Blog not found")
    
    db.delete(blog)
    db.commit()

    return {
        "data": f"Deleted Successfully"
    }

@router.patch("/{id}")
def update_blog(id: int,title: Optional[str] = None, content: Optional[str] = None, db : Session = Depends(get_db)):

    blog = db.query(Blog).filter(Blog.id == id).first()

    if blog is None:
        return HTTPException(status_code=404, detail="Blog Not Found")
    
    if title:
        blog.title = title
    if content:
        blog.content = content

    db.commit()

    db.refresh(blog)
    return {
        "Data" : blog
    }