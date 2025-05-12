
from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(
    tags = ["Blogs"],
    prefix='/blogs'
)

@router.get("/")
def get_blogs(limit : Optional[str] = None):
    return {
        "data" : [
            {
                "Title": f"First Blog {limit}"
            }
        ]
    }

class Blog(BaseModel):
    title : str
    body: str


@router.post("/")
def create(request : Blog):
    return {
        "data" : f"Created {request}"
    }


@router.delete("/{id}")
def delete_blog(id : int):
    return {
        "data": f"Deleted Successfully : {id}"
    }

@router.patch("/{id}")
def update_blog(id: int):
    return {
        "Data" : f"Updated Successfully : {id}"
    }