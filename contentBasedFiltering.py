from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv("articles.csv", low_memory=False)
df.dropna()

count = CountVectorizer(stop_words="english")
count_matrix = count.fit_transform(df["title_cl"].values.astype('U'))

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
indices = pd.Series(df.index, index=df['title'])

def get_recommendation(title, cosine_sim):
    idx=indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    #print(df['title'].iloc[movie_indices])
    return (df['title'].iloc[movie_indices])

get_recommendation("deepmind moves to tensorflow", cosine_sim2) 