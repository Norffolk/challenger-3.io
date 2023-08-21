# How to create a simple app using python (with flask framework)

**1. After python3 is installed, create a new folder:**
```
mkdir meusite
```
**2. Install the python3 venv (virtual environment):**
```
sudo apt install python3-venv
```
**3. to create the virtual environment:**
```
python3 -m venv env
```
**4. to activate and deactivate the virtual environment:**
```
source env/bin/activate
or 
deactivate
```
**5. now we need install flask with this command:**
```
pip install flask
```
**6. finally, you can create the python code (a simple example):**
```
sudo vi app.py >>

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

app.run(host='0.0.0.0', port=81)
```
**7. to run this code, first we need export and run:**
```
export FLASK_APP=app.py
```
``and``
```
flask run
```
**8. replace my original code app in the app.py:**
```
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
```
**9. create a index.html in folder call "templates":**
```
mkdir templates && cd templates && sudo vi index.html
```
``and put the content:``
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>{{ variavel }}</h1>
    <form action="{{ url_for('index') }}" method="post">
        <label for="">Número:</label><br>
        <input type="text" name="name" placeholder="Insira um número">
        <button>Enviar</button>
    </form>
</body>
</html>
```
**10. run flask run again:**
```
flask run
```
``open the browser with localhost:5000 or 127.0.0.1``
