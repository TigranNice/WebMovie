from fastapi import APIRouter, Depends

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import UserRatingsSchema, Answer, AnswerRecommend
from .models import UserRecommendation, Movie, UserRatings, MovieRating
from .utils import check_genres
from ..database import get_async_session
from ..recommendation_system.recommend_similar.similar import get_recommendation

router = APIRouter(
    prefix="/recommend",
    tags=["recommend"],
)


@router.get("/get_best_by_genres")
async def get_best_by_genres(genres: str,
                             session: AsyncSession = Depends(get_async_session)) -> AnswerRecommend | Answer:
    """
    Retrieves the best movies by genres.

    Args:
        genres (str): A comma-separated string of genres.
        session (AsyncSession, optional): The async database session. Defaults to Depends(get_async_session).

    Returns:
        AnswerRecommend | Answer: An instance of AnswerRecommend if successful,
         or an instance of Answer if unsuccessful.

    Raises:
        None

    """
    genres = genres.split(",")
    if genres is None:
        return Answer(status="unsuccessful", problem="no genres provided")

    # check if genres are valid
    check, genre = check_genres(genres)
    if not check:
        return Answer(status="unsuccessful", problem=f"invalid genre: {genre}")

    # Create the sort conditions
    sort_conditions = []
    for genre in genres:
        sort_conditions.append(getattr(MovieRating, f"{genre.lower()}").desc())
    sort_conditions.append(MovieRating.rating.desc())

    try:
        stmt = select(MovieRating.title, MovieRating.rating, MovieRating.year, MovieRating.description).order_by(
            *sort_conditions).limit(10)

        # Retrieve the top 10 results
        result = await session.execute(stmt)
        result = result.scalars().all()
        return AnswerRecommend(status="successful", data=result)
    except Exception as e:
        print(e)
        return Answer(status="unsuccessful", problem="problem on the server")


@router.get("/get_recommend_similar")
async def get_recommend_similar(genres: str,
                                session: AsyncSession = Depends(get_async_session)) -> AnswerRecommend | Answer:
    """
    Retrieves recommendations for movies similar to the provided genres.

    Args:
        genres (str): A comma-separated string of genres.
        session (AsyncSession, optional): An async session to interact with the database.
        Defaults to Depends(get_async_session).

    Returns:
        AnswerRecommend or Answer:
        An instance of AnswerRecommend if the operation is successful,
         containing a list of movie titles;
         otherwise, an instance of Answer with the corresponding error message.
    """
    genres = genres.split(",")
    if genres is None:
        # TODO: return global average
        return Answer(status="unsuccessful", problem="no genres provided")

    # check if genres are valid
    check, genre = check_genres(genres)
    if not check:
        return Answer(status="unsuccessful", problem=f"invalid genre: {genre}")

    try:
        # find similar users
        user_id = get_recommendation(genres)
        print(user_id)
        # get recommendations
        recommendation = await session.get(UserRecommendation, user_id)
        rec = eval(recommendation.items)
        movie_id = [i[0] for i in rec]
        # get movies title
        stmt = select(Movie.title).where(Movie.id.in_(movie_id))
        movies_title = await session.execute(stmt)
        return AnswerRecommend(status="successful", data=movies_title.scalars().all())
    except Exception as e:
        print(e)
        return Answer(status="unsuccessful", problem="problem on the server")


@router.post("/post_recommend")
async def post_recommend(request: UserRatingsSchema, session: AsyncSession = Depends(get_async_session)) -> Answer:
    """
    Endpoint for posting recommendations.

    Args:
        request (UserRatingsSchema): The request object containing user ratings.
        session (AsyncSession): The async database session.

    Returns:
        Answer: The response object indicating the success or failure of the operation.
    """
    # TODO: test it
    try:
        # check if movie and rating are the same length
        if len(request.movie) != len(request.rating):
            return Answer(status="unsuccessful", problem="movie and rating must be the same length")

        # insert data
        stmt = []
        for i in range(len(request.movie)):
            stmt.append({"user_id": request.user_id, "movie_id": request.movie[i], "rating": request.rating[i]})
        await session.execute(insert(UserRatings).values(stmt))
        await session.commit()
        return Answer(status="successful")

    except Exception as e:
        print(e)
        return Answer(status="unsuccessful", problem="problem on the server")
