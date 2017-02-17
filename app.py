from flask import Flask, render_template, request
from text_generator import TextGenerator


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def mrkov_chain_text():
    if request.method == "GET":
        return render_template("index.html", markov_chain_texts = '文章を生成します。')
    elif request.method == "POST":
        keyword = request.form['keyword']
        generator = TextGenerator()
        markov_chain_texts = generator.generate(keyword)
        return render_template("index.html", keyword=keyword, markov_chain_texts=markov_chain_texts)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
