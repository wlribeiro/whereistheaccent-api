from fastapi import APIRouter, status, HTTPException

from whereistheaccent import models, repository
from whereistheaccent.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()



@router.get('/words/all')
def list_all_words(): 
    result = repository.get_all_words(get_db())

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Words not found"
        )
    return result


@router.get('/words/accented')
async def get_accented_words():
    result = repository.get_accented_words(get_db())

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Words not found"
        )
    return result
