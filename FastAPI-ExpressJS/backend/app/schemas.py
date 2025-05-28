from typing import Optional
from sqlmodel import SQLModel

class MovieCreate(SQLModel):
    title: str
    director: str
    year: int

class MovieUpdate(SQLModel):
    title: Optional[str] = None
    director: Optional[str] = None
    year: Optional[int] = None
