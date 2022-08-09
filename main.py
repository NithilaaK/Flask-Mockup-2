from flask import Flask, jsonify, request
import csv
from flask_cors import CORS

from storage import all_articles, liked_articles, not_liked_articles
from demographicFiltering import output
from contentBasedFiltering import get_recommendation

app = Flask(__name__)
CORS(app)

@app.route("/get-article")
def get_article():
    article_data = {
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13],
        "lang": all_articles[0][14],
        "total_events": all_articles[0][15]
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        dat = {
            "url": article[0],
            "title": article[1],
            "text": article[2],
            "lang": article[3],
            "total_events": article[4]
        }
        article_data.append(dat)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:    
        output = get_recommendation(liked_article[4])
        for data in output:
            all_recommended.append(data)
    all_recommended.sort()
    import itertools as it
    all_recommended = list(all_recommended for all_recommended,_ in it.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        dat = {
            "url": recommended[0],
            "title": recommended[1],
            "text": recommended[2],
            "lang": recommended[3],
            "total_events": recommended[4]
        }
        article_data.append(dat)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

if __name__ == "__main__":
    app.run()