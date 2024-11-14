from .. import schemas
from sqlalchemy.orm import Session
from ..hashing import Hash
from .. import model
from fastapi import HTTPException, status
from fastapi import APIRouter,Depends, status, HTTPException, Response
from .. import schemas, database

get_db= database.get_db

def create(request: schemas.User, db: Session = Depends(get_db)):
    new_user = model.User(name=request.name,
                           email=request.email,
                             password=Hash.scrape(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(id: int, db: Session):
    user = db.query(model.User).filter(model.User.id ==id).first()
    if user == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"USER with the id {id} you are requesting for doeant exist")

    return user