# # app/api.py or similar
# from fastapi import APIRouter, Depends, HTTPException
# from app.database import get_session
# from app.schemas import MovieCreate, MovieUpdate
# from app.crud import create_movie, get_movies, get_movie, update_movie, delete_movie
# from sqlmodel import Session

# router = APIRouter()

# @router.post("/movies/")
# def add_movie(movie: MovieCreate, session: Session = Depends(get_session)):
#     return create_movie(session, movie)

# @router.get("/movies/")
# def list_movies(session: Session = Depends(get_session)):
#     return get_movies(session)

# @router.get("/movies/{movie_id}")
# def get_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
#     movie = get_movie(session, movie_id)
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return movie

# @router.put("/movies/{movie_id}")
# def update_movie_by_id(movie_id: int, movie_data: MovieUpdate, session: Session = Depends(get_session)):
#     movie = update_movie(session, movie_id, movie_data)
#     if not movie:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return movie

# @router.delete("/movies/{movie_id}")
# def delete_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
#     success = delete_movie(session, movie_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return {"ok": True}

from fastapi import APIRouter, Depends, HTTPException
from app.database import get_session
from app.schemas import MovieCreate, MovieUpdate
from app.crud import create_movie, get_movies, get_movie, update_movie, delete_movie
from sqlmodel import Session

router = APIRouter()
@router.post("/movies/")
def add_movie(movie: MovieCreate, session: Session = Depends(get_session)):
    return create_movie(session, movie)

@router.get("/movies/")
def list_movies(session: Session = Depends(get_session)):
    return get_movies(session)

@router.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
    print(f"Fetching movie id={movie_id}")
    movie = get_movie(session, movie_id)
    if not movie:
        print(f"Movie id={movie_id} not found")
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.put("/movies/{movie_id}")
def update_movie_by_id(movie_id: int, movie_data: MovieUpdate, session: Session = Depends(get_session)):
    movie = update_movie(session, movie_id, movie_data)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@router.delete("/movies/{movie_id}")
def delete_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
    success = delete_movie(session, movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"ok": True}