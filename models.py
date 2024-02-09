import datetime
from typing import List, Annotated
from bson import Decimal128, ObjectId
from pydantic import BaseModel, ConfigDict, Field, PlainSerializer
from pydantic_mongo import AbstractRepository, ObjectIdField

Decimal128Float = Annotated[
    Decimal128,
    PlainSerializer(lambda x: x.to_decimal, return_type=float)
]

class Comment(BaseModel):
    body: str
    email: str
    author: str

class Post(BaseModel):
    id: ObjectIdField = ObjectId
    body: str = Field(...)
    permalink: str
    author: str
    title: str = Field(...)
    tags: List[str] = Field(...)
    comments: List[Comment] = Field(...)
    date: datetime.datetime = Field(
        description="Date the post was written"
    )

class PostRepository(AbstractRepository[Post]):
    class Meta:
        collection_name = "posts"
