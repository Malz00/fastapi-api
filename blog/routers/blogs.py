from fastapi import APIRouter,Depends, status, HTTPException, Response
from .. import schemas, database, model
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog
from ..oauth2 import get_current_user

router = APIRouter(
    prefix = "/blog",
    tags=["Blogs"]
)

get_db = database.get_db


@router.get('', response_model=None)
def all(db: Session = Depends(get_db), current_user: schemas.User =Depends(get_current_user) ):
    
    return blog.get_all(db)

@router.post('', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db), current_user: schemas.User =Depends(get_current_user) ):
   
   return blog.create(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(database.get_db), current_user: schemas.User =Depends(get_current_user) ):
   
   return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db:Session = Depends(get_db), current_user: schemas.User =Depends(get_current_user) ):
    
    return blog.update(db, id)



@router.get('/{id}', status_code=200, response_model=None )
def show(id, responses: Response, db:Session=Depends(get_db)):
   
   return blog.show(id, db)




# @app.get('/blog', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(model.Blog).all()
#     return blog