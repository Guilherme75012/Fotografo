from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("./Html/Index.html", Titulo="Bem vindo ao site de Pokémon")

if __name__ == '__main__':
    app.run()
