from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    x = "hello worlcddd"
    return render_template("index.html", show=x)


@app.route("/hello/<user>")
def hello(user):
    return render_template("hello.html", name=user)


@app.route("/hello/<user2>")
def hello3(user2):
    return render_template("hello.html", name=user2)


@app.route("/helloo/<user2>")
def hello2(user2):
    x = [1, 2, 4, 6, 7, 8]
    return render_template("index2.html", name=x)


# @app.route('/',methods=['Get','Post'])
# def index()
#     if request.method == ''


if __name__ == "__main__":
    app.debug = True
    app.run()

