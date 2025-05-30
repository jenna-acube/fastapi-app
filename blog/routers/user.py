from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from .. import schemas, models
from ..database import get_db
from typing import List
from ..hashing import Hash
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"],
    responses={404: {"description": "Not found"}}
)


@router.post('/', response_model=schemas.ShowUserDetail, status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', response_model=schemas.ShowUserDetail)
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id, db)