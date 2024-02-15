import pandas as pd
import numpy as np

unique_genres = ['Adventure', 'Animation', 'Children', 'Comedy', 'Fantasy', 'Romance', 'Drama', 'Action', 'Crime',
                 'Thriller', 'Horror', 'Mystery', 'Sci-Fi', 'War', 'Musical', 'Documentary', 'Western', 'Film-Noir']


def user_genre_to_all(user: list[str]) -> np.ndarray:
    """
    Generates a numpy array representing the user's genre preferences.

    Args:
        user (list[str]): A list of strings representing the user's preferred genres.

    Returns:
        np.ndarray: A numpy array representing the user's genre preferences.
    """
    user_genres = pd.DataFrame([[0] * len(unique_genres)], columns=unique_genres)
    line = iter(range(len(user), 0, -1))
    for genre in user:
        user_genres[genre] = next(line)
    return user_genres.to_numpy()[0]


def find_similar(user: np.ndarray) -> int:
    """
    Find the most similar user based on their movie preferences.

    Args:
        user (ndarray): An array representing the movie preferences of the user.

    Returns:
        int: The ID of the most similar user.
    """
    # load other users
    data = pd.read_csv("src/recommendation_system/recommend_similar/data/norm_user-genres.csv")
    # normalize user
    user = user / np.linalg.norm(user)

    max_val = 0
    user_id = 0

    # find the most similar user
    for i in range(len(data)):
        movies = data.iloc[i]
        val = np.dot(user, movies)
        if val > max_val:
            max_val = val
            user_id = i + 1
    return user_id


def get_recommendation(genres: list[str]) -> int:
    new_user = user_genre_to_all(genres)
    new_user = find_similar(new_user)
    return new_user
