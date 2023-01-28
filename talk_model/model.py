import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import BallTree
from sklearn.pipeline import make_pipeline

data = pd.read_csv('talk_model/good.tsv', sep='\t')
data.head()

vect = TfidfVectorizer()

vect.fit(data.context_0)

matrix_big = vect.transform(data.context_0)
print(matrix_big.shape)
svd = TruncatedSVD(n_components=300)
svd.fit(matrix_big)

matrix_small = svd.transform(matrix_big)

print(matrix_small.shape)
print(svd.explained_variance_ratio_.sum())


def softmax(x):
    proba = np.exp(-x)
    return proba / sum(proba)


class NeighborSampler(BaseEstimator):
    def __init__(self, k=5, temperature=1.0):
        self.k = k
        self.temperature = temperature

    def fit(self, X, y):
        self.tree_ = BallTree(X)
        self.y_ = np.array(y)

    def predict(self, X, random_state=None):
        distances, indices = self.tree_.query(X, return_distance=True, k=self.k)
        result = []
        for distance, index in zip(distances, indices):
            result.append(np.random.choice(index, p=softmax(distance * self.temperature)))
        return self.y_[result]


ns = NeighborSampler()
ns.fit(matrix_small, data.reply)

pipe = make_pipeline(vect, svd, ns)
