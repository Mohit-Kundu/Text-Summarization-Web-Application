from flask import Flask, render_template, request, url_for
from scraper import scraper
from summarizer import summarizer

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        title, text = scraper(url)
        summary = summarizer(text)
        summary_html = '<textarea>' + summary + '</textarea>'
        return summary

    else: 
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True) 