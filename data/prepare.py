from surprise import Dataset, Reader, SVD

import pandas as pd
import pickle

data = pd.read_csv("data/ratings.csv")

reader = Reader(rating_scale=(1, 5))

data = Dataset.load_from_df(data[["userId", "movieId", "rating"]], reader)


trainset = data.build_full_trainset()


algo = SVD(n_factors=100, n_epochs=20, lr_all=0.005, reg_all=0.02)

algo.fit(trainset)

with open("model.pkl", "wb") as f:
    pickle.dump(algo, f)

testset = trainset.build_testset()

predictions = algo.test(testset)

with open("predictions.pkl", "wb") as f:
    pickle.dump(predictions, f)