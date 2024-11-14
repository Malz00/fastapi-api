
from sqlalchemy.orm import Session

from .. import model

from .. import schemas
from fastapi import HTTPException, status

def get_all(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session):
    new_blog = model.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(db: Session, id:int):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found ")
    else:
        blog.delete(synchronize_session=False)
        db.commit()

    return 'done'

def update(request: schemas.Blog,db: Session, id: int):
    blog = db.query(model.Blog).filter(model.Blog.id == id)
    if  not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"blog with id {id} not in database ")
    else:

        blog.update(request)
        db.commit()
    return "this has been updated"


def show(db: Session, id: int ):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()
    if not blog:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} you are requesting for doeant exist")
        
    return blog
