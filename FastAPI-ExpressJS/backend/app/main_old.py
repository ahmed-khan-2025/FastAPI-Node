from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.database import create_db_and_tables, get_session
from app.schemas import MovieCreate, MovieUpdate
from app.crud import create_movie, get_movies, get_movie, update_movie, delete_movie
from sqlmodel import Session
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/movies/")
def add_movie(movie: MovieCreate, session: Session = Depends(get_session)):
    return create_movie(session, movie)

@app.get("/movies/")
def list_movies(session: Session = Depends(get_session)):
    return get_movies(session)

@app.get("/movies/{movie_id}")
def get_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
    print(f"Fetching movie id={movie_id}")
    movie = get_movie(session, movie_id)
    if not movie:
        print(f"Movie id={movie_id} not found")
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.put("/movies/{movie_id}")
def update_movie_by_id(movie_id: int, movie_data: MovieUpdate, session: Session = Depends(get_session)):
    movie = update_movie(session, movie_id, movie_data)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@app.delete("/movies/{movie_id}")
def delete_movie_by_id(movie_id: int, session: Session = Depends(get_session)):
    success = delete_movie(session, movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"ok": True}

