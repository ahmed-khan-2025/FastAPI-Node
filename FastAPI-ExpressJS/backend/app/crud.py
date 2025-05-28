from sqlmodel import Session, select
from app.models import Movie
from app.schemas import MovieCreate, MovieUpdate  # assuming you have MovieUpdate schema

def create_movie(session: Session, movie_data: MovieCreate) -> Movie:
    movie = Movie.from_orm(movie_data)
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie

def get_movies(session: Session):
    return session.exec(select(Movie)).all()

def get_movie(session: Session, movie_id: int) -> Movie | None:
    return session.get(Movie, movie_id)

def update_movie(session: Session, movie_id: int, movie_data: MovieUpdate) -> Movie | None:
    movie = session.get(Movie, movie_id)
    if not movie:
        return None
    if movie_data.title is not None:
        movie.title = movie_data.title
    if movie_data.director is not None:
        movie.director = movie_data.director
    if movie_data.year is not None:
        movie.year = movie_data.year
    session.add(movie)
    session.commit()
    session.refresh(movie)
    return movie

def delete_movie(session: Session, movie_id: int) -> bool:
    movie = session.get(Movie, movie_id)
    if not movie:
        return False
    session.delete(movie)
    session.commit()
    return True
