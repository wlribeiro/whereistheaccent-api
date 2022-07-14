from sqlalchemy.orm import Session

from whereistheaccent import models, schemas


def get_accented_words(db: Session):
    return db.query(models.Word).filter(models.Word.is_accented == 1).all()


def get_all_words(db: Session):
    return db.query(models.Word).all()

# def get_words(db: Session, skip: int = 0, limit: int = 100000):
#     return db.query(models.Word).filter(models.Word.is_accented == 1).offset(skip).limit(limit).all()

def create_word(db: Session, word: schemas.WordCreate):
    db_word =  models.Word(word=word.get('word'), is_accented='1' if word.get('is_accented')else '0')
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word
