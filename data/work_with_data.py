import pickle
from utils import get_top_n
import pandas as pd

def movieid_genres():
    """
    This function reads the "movies.csv" file and extracts the columns "movieId" and "genres". 
    It then splits the "genres" column by "|" and expands the dataframe so that each row contains 
    a single genre. Finally, it saves the resulting dataframe to "movieid-genres.csv" without including 
    the index.
    """
    data = pd.read_csv("data/movies.csv")

    data = data[["movieId", "genres"]]
    data.genres = data.genres.str.split("|")
    data = data.explode("genres")

    data.to_csv("data/movieid-genres.csv", index=False)


def unique_genres():
    """
    Function to read movie genres from a CSV file, extract unique genres, remove specific genres, 
    and save the unique genres to a new CSV file.
    No parameters or return types specified.
    """
    data = pd.read_csv("data/movieid-genres.csv")

    unique_genres = data.genres.unique()
    unique_genres = list(unique_genres)
    del unique_genres[-1]
    del unique_genres[-3]

    pd.DataFrame(unique_genres, columns=["genres"]).to_csv("data/unique-genres.csv", index=False)


def recommendation_system(user_id):

    with open("predictions.pkl", "rb") as f:
        predictions = pickle.load(f)


    top_n = get_top_n(predictions, n=10)

    lst = []

    for uid, user_ratings in top_n.items():
        for iid, rating in user_ratings:
            lst.append((uid, iid, rating))

    recomended = pd.DataFrame(lst, columns=["userId", "movieId", "rating"])
    recomended.to_csv("data/recomended.csv", index=True)


def user_movies():
    data = pd.read_csv("data/ratings.csv")

    data = data[["userId", "movieId"]]

    data = data.groupby("userId")["movieId"].apply(list)

    data = data.to_dict()
    u_genres = pd.read_csv("data/unique-genres.csv")["genres"].to_list()
    user_genres = pd.DataFrame([[0] * len(u_genres)] * len(data), columns=u_genres, index=data.keys())

    genres = pd.read_csv("data/movieid-genres.csv")
    for user_id, list_movie in data.items():
        for movie in list_movie:
            for genre in genres[genres.movieId == movie]["genres"]:
                if genre in user_genres.columns:
                    user_genres.at[user_id, genre] += 1
    user_genres.to_csv("data/user-genres.csv", index=False)


def clear_imdb():
    data = pd.read_csv("data/imdb_top_1000.csv")

    data = data[["Series_Title", "Released_Year", "Genre", "IMDB_Rating", "Overview"]]

    data.to_csv("data/rr.csv", index=False)


clear_imdb()