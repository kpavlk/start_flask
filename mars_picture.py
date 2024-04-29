from flask import Flask, url_for
from flask import request

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

@app.route("/astronaut_selection", methods=['POST', 'GET'])
def astronaut_selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Пример формы</title>
                              </head>
                              <body>
                                <h3>Анкета претендента</h3>
                                <h4>на участие в миссии</h4>
                                <div>
                                    <form class="login_form" method="post">
                                        <input type="surname" class="form-control" id="surname" placeholder="Введите фамилию" name="surname">
                                        <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="classSelect">Какое у вас образование?</label>
                                            <select class="form-control" id="classSelect" name="class">
                                              <option>Начальное</option>
                                              <option>Основное</option>
                                              <option>Среднее</option>
                                              <option>Высшее</option>
                                            </select>
                                         </div>
                                         <div class="form-group">
                                            <label for="professions">Какие у вас профессии?</label>
                                            <div class="form-check">
                                            <input type="checkbox" class="form-check-input" id="p1" name="ingeneer">
                                            <label class="form-check-label" for="p1">Инженер-исследователь</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="p2" name="ingeneer1">
                                            <label class="form-check-label" for="p2">Инженер-строитель</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="p3" name="ingeneer2">
                                            <label class="form-check-label" for="p3">Пилот</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="ingeneer" name="ingeneer">
                                            <label class="form-check-label" for="acceptRules">Метеоролог</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="ingeneer" name="ingeneer">
                                            <label class="form-check-label" for="acceptRules">Инженер по жизнеобеспечению</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="ingeneer" name="ingeneer">
                                            <label class="form-check-label" for="acceptRules">Инженер по радиационной защите</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="ingeneer" name="ingeneer">
                                            <label class="form-check-label" for="acceptRules">Врач</label>
                                            <br>
                                            <input type="checkbox" class="form-check-input" id="ingeneer" name="ingeneer">
                                            <label class="form-check-label" for="acceptRules">Экзобиолог</label>
                                            </div>
                                        </div>
                                         <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <div class="form-group">
                                            <label for="about">Почему вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")

