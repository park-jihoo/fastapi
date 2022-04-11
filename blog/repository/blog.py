from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, models


def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def create(request: schemas.Blog, db: Session, user: schemas.User):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=user.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")

    blog.delete(synchronize_session=False)
    db.commit()
    return {'done'}


def update(id, request: schemas.Blog, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")

    blog.update(request)
    db.commit()
    return {'updated'}


def show(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with the id {id} is not available")
    return blog
