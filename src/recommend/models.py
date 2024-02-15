from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    genres: Mapped[str]


class MovieRating(Base):
    __tablename__ = "movie_ratings"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    year: Mapped[int]
    rating: Mapped[float]
    description: Mapped[str]
    action: Mapped[int]
    adventure: Mapped[int]
    animation: Mapped[int]
    biography: Mapped[int]
    comedy: Mapped[int]
    crime: Mapped[int]
    drama: Mapped[int]
    family: Mapped[int]
    fantasy: Mapped[int]
    film_noir: Mapped[int]
    history: Mapped[int]
    horror: Mapped[int]
    music: Mapped[int]
    musical: Mapped[int]
    mystery: Mapped[int]
    romance: Mapped[int]
    sci_fi: Mapped[int]
    sport: Mapped[int]
    thriller: Mapped[int]
    war: Mapped[int]
    western: Mapped[int]


class UserRatings(Base):
    __tablename__ = "user_ratings"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]
    movie_id: Mapped[int] = mapped_column(ForeignKey("movies.id"))
    rating: Mapped[float]


class UserRecommendation(Base):
    __tablename__ = "user_recommendation"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    items: Mapped[str]
