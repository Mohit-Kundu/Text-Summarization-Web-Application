from flask import Flask, render_template, request, url_for
from scraper import scraper

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        #return url
        title, text = scraper(url)
        return title,text
        

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True) 