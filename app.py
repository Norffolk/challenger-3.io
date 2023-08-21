from flask import Flask, render_template, request
from random import randint

app=Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    variavel = "Game: Adivinhe o número correto"

    if request.method == "GET":
        return render_template("index.html", variavel=variavel)
    else:
        numero = randint(1,20)
        palpite = int(request.form.get("name"))
        if numero == palpite:
            return '<h1>Resultado: Você ganhou!</h1>'
        else:
            return '<h1>Resultado: Você perdeu!</h1>'
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
