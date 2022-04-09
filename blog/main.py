from fastapi import FastAPI
from . import schemas, models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post("")
def create(request: schemas.Blog):
    return {'title': request.title, 'body': request.body}
