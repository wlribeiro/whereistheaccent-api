import re
import requests
from sqlalchemy.orm import Session

from whereistheaccent import models, repository, schemas
from whereistheaccent.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


def search_words(text:str) -> list:
    return re.findall('\w+', text)


def has_accent(word:str) -> bool:
    return True if re.search('[À-ü]', word) else False


if __name__ == '__main__':
    url = 'https://www.ime.usp.br/~pf/dicios/br-utf8.txt'

    response = requests.get(url)
    if not response.status_code == 200 :
        exit(
            f'An error has occurred when trying to collect datas [status code: {response.status_code}]'
        )

    words = search_words(response.text)

    db: Session = get_db()
    for word in words:
        word_dict:schemas.WordCreate = {
            'word': word, 
            'is_accented': False
            }
        
        if has_accent(word):
            word_dict = {
                **word_dict,
                'is_accented': True
            }
        repository.create_word(
                db=db,
                word=word_dict
                )
        print(word_dict)

