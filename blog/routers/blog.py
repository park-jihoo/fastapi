from typing import List

from fastapi import Depends, status, Response, APIRouter
from sqlalchemy.orm import Session

from .. import schemas, database, oauth2
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['blogs']
)

get_db = database.get_db



@router.get("/", response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.create(request, db, current_user)


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.show(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def destroy(id:int , db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)
