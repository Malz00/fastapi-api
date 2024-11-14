from fastapi import FastAPI
from typing import Optional

from pydantic import BaseModel

import uvicorn

app = FastAPI()

#?limit=10&published=true'

@app.get('/blog')
def index(limit, published):
    # only get 10 
    if published:

        return {'data': {'name':f'{limit} blogs from the db '}}
    else:
        return{'data': f'{limit} blogs from th db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blog'}


@app.get('/blog/{id}')
def show(id:int ):
    return {'data':id}




@app.get('/blog/{id}/comments')
def comments(id):
    return{'data':{'what', 'you', 'do'}}


class Blog(BaseModel):
    tile: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return {'data':'blog is created witth title as {blog.title}'}



# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=7000)