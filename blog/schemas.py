from pydantic import BaseModel
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUserDetail(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []

    class Config():
        orm_mode = True

class ShowUserName(BaseModel):
    name: str

    class Config():
        orm_mode = True

class ShowAllBlog(BaseModel):
    title: str
    body: str
    creator: ShowUserDetail
    
    class Config():
        orm_mode = True        

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUserName
    
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None