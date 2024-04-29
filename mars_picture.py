from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def page():
    return "Миссия Колонизация Марса"


@app.route("/index")
def index():
    return "И на Марсе будут яблони цвести!"


@app.route("/promotion")
def promotion():
    slogans = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
               "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]

    return '<br>'.join(slogans)


@app.route("/image_mars")
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"/>
                    <br> Вот она какая, красная планета.
                  </body>
                </html>"""


@app.route("/promotion_image")
def promotion_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                   <link rel="stylesheet" href="static/css/style.css">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}"/>
                    <div class="alert alert-secondary" role="alert">
                      <h3>Человечество вырастает из детства.</h3>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h3>Человечеству мала одна планета.</h3>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h3>И начнём с Марса!</h3>
                    </div>
                    <div class="alert alert-danger " role="alert">
                      <h3>Присоединяйся!</h3>
                    </div>
                  </body>
                </html>"""


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

