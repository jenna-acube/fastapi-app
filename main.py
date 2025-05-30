from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

import uvicorn

app = FastAPI()


@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None): 
    # fetch blogs with limit and published status
    if published:
        return {"data": f'{limit} published blogs from db'}
    else:
        return {"data": f'{limit} blogs from db'}


@app.get("/blog/unpublished")
def unpublished():
    # fetch unpublished blogs
    return {"data": 'all unpublished blogs'}


@app.get("/blog/{id}")  
def show(id: int):
    # fetch blog with id = id
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    # fetch comments of blog with id = id
    return {"data": {'1', '2'}} 


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]



@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f'Blog created is created with title as {request.title}'}

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)
# To run the server, use the command: uvicorn main:app --reload
# To test the API, you can use a tool like Postman or curl.
# You can also test the API using the command line with curl:
# curl -X GET "http://