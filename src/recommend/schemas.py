from pydantic import BaseModel, confloat

from enum import Enum


class Genre(str, Enum):
    action = "Action"
    adventure = "Adventure"
    animation = "Animation"
    children = "Children"
    comedy = "Comedy"
    crime = "Crime"
    documentary = "Documentary"
    drama = "Drama"
    fantasy = "Fantasy"
    film_noir = "Film-Noir"
    horror = "Horror"
    musical = "Musical"
    mystery = "Mystery"
    romance = "Romance"
    scifi = "Sci-Fi"
    thriller = "Thriller"
    war = "War"
    western = "Western"


class RequestGenres(BaseModel):
    genres: list[Genre]


class UserRatingsSchema(BaseModel):
    user_id: int
    movie: list[str] = []
    rating: list[confloat(ge=1, le=5)] = []


# TODO: use it
class RecommendStatus(str, Enum):
    successful = "successful"
    unsuccessful = "unsuccessful"


class Answer(BaseModel):
    status: str
    problem: str | None = None


class AnswerRecommend(Answer):
    data: list[str]
