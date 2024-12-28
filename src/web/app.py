from flask import Flask, render_template, jsonify
from src.selenium.twitter_scraper import scrape_trending_topics
from src.database.mongo_utils import fetch_latest_record

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run-script', methods=['GET'])
def run_script():
    result = scrape_trending_topics()
    return jsonify(result)

@app.route('/latest-result', methods=['GET'])
def latest_result():
    result = fetch_latest_record()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
