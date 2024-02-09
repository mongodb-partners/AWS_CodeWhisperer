from bson.objectid import ObjectId
from fastapi import APIRouter, Request,  HTTPException, status
from typing import List
from models import Post

router = APIRouter()

@router.get("/", response_description="List all posts", response_model=List[Post])
def list_posts(request: Request):
    posts = list(request.app.db["posts"].find(limit=100))
    return posts

@router.get("/{id}", response_description="Get a single post by id", response_model=Post)
def find_post(id: str, request: Request):
    if ObjectId.is_valid(id) is False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid ID {id}. Post not found" )

    if (post := request.app.db["posts"].find_one({"_id": ObjectId(id)})) is not None:
        return post
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with ID {id} not found")
