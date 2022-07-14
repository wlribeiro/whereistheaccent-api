from fastapi import FastAPI, status, HTTPException
from sqlalchemy.orm import Session

from whereistheaccent import models, repository
from whereistheaccent.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

cache = []

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


@app.get('/')
def index():
    return {'message': 'hello world'}

@app.get('/words/all')
def list_all_words(): 
    global cache
    if cache :
        return cache
    
    result = repository.get_all_words(get_db())

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Words not found"
        )
    cache = result
    return result


@app.get('/words/accented')
async def get_accented_words():
    global cache
    if cache :
        return cache
    
    result = repository.get_accented_words(get_db())

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Words not found"
        )
    cache = result
    return result
