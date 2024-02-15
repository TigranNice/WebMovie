from src.recommend.schemas import Genre


def check_genres(genres: list[str]):
    r_genres = set(i.value for i in Genre)
    print(r_genres)
    for genre in genres:
        if genre not in r_genres:
            return False, genre
    return True, None
