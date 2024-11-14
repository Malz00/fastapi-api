from fastapi import APIRouter,Depends, status, HTTPException, Response
from .. import schemas, database, model
from typing import List
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..repository import users

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

get_db = database.get_db


                               
@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db:Session=Depends(get_db)):
    
    return users.create(db, request)


@router.get('/{id}',  response_model=schemas.ShowUser)
def get_user(id:int , db:Session = Depends(get_db)):
   
   return users.show(id, db)


