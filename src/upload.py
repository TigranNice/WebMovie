# DON'T USE IT

from sqlalchemy import create_engine
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

"""
with open("E:/Tigran/VSPython/WebMovie/data/rr_cleared.csv", "r") as f:
    conn = create_engine(DATABASE_URL).raw_connection()
    cursor = conn.cursor()
    cmd = ('COPY movie_ratings(title, year, rating, description, action, adventure, animation, biography, comedy, '
           'crime, drama, family, fantasy, film_noir, history, horror, music, musical, mystery, romance, sci_fi, '
           'sport, thriller, war, western) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ",")')
    cursor.copy_expert(cmd, f)
    conn.commit()


with open("E:/Tigran/VSPython/WebMovie/data/top_10.csv", "r") as f:
    conn = create_engine(DATABASE_URL).raw_connection()
    cursor = conn.cursor()
    cmd = 'COPY user_recommendation(user_id, items) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ",")'
    cursor.copy_expert(cmd, f)
    conn.commit()



with open("movies.csv", 'r') as f:
    conn = create_engine(DATABASE_URL).raw_connection()
    cursor = conn.cursor()
    cmd = 'COPY movies(id, title, genres) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ",")'
    cursor.copy_expert(cmd, f)
    conn.commit()


with open("ratings.csv", 'r') as f:
    conn = create_engine(DATABASE_URL).raw_connection()
    cursor = conn.cursor()
    cmd = 'COPY user_ratings(id, user_id, movie_id, rating) FROM STDIN WITH (FORMAT CSV, HEADER TRUE, DELIMITER ",")'
    cursor.copy_expert(cmd, f)
    conn.commit()
"""
