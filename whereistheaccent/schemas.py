from typing import Optional
from pydantic import BaseModel


class WordBase(BaseModel):
    name: str
    is_accented: Optional[int] = 0

class WordCreate(WordBase):
    pass
