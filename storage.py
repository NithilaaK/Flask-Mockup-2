from csv import reader

all_articles = []

with open('articles.csv', encoding="utf8") as f:
    csvreader = reader(f)
    data = list(csvreader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []