from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app=FastAPI()

class MovieUpdate(BaseModel):
    title:str
    director:str
    genre:str
    language:str
    release_year:int
    is_available:bool

movies = [
 {
 "id": 1,
 "title": "3 Idiots",
 "director": "Rajkumar Hirani",
 "genre": "Comedy Drama",
 "language": "Hindi",
 "release_year": 2009,
 "is_available": True
 },
 {
 "id": 2,
 "title": "Baahubali",
 "director": "S S Rajamouli",
 "genre": "Action Drama",
 "language": "Telugu",
 "release_year": 2015,
 "is_available": True
 }
]

@app.get("/")
def home():
    return {"message":"Movie API is Running"}

@app.get("/movies")
def get_movie():
    return movies

@app.put("/movies/{movie_id}")
def update_movie(movie_id : int , movie : MovieUpdate):
    for existing_movie in movies:
        if existing_movie["id"]==movie_id:
            existing_movie.update(movie.model_dump())
            return{
                "message":"Movie updated successfully",
                "movie":existing_movie
            }
    raise HTTPException(status_code=404,detail="Movie not found")
