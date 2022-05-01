from flask import Flask, render_template, request, redirect, abort
import os
import json

def LeerLibreria():
    try:
        f=open("MSX.json")
        datos = json.load(f)
        f.close
        return datos
    except:
        print("Error al leer el fichero")

msxjuegos=LeerLibreria()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")

@app.route('/juegos', methods=['POST'])
def juegos_post():
    libreria = []
    buscadorjuegos = request.form['juego']
    for juego in msxjuegos:
        nombre= str(juego.get("nombre"))
        if nombre.startswith(str(buscadorjuegos)):
            dict={"nombre":juego.get("nombre"),"desarrollador":juego.get("desarrollador"),"id":juego.get("id")}
            libreria.append(dict)
    return render_template("listajuegos.html", msxjuegos=libreria , buscadorjuegos=buscadorjuegos)



#port=os.environ["PORT"]
#app.run("0.0.0.0",int(port),debug=True)
app.run("0.0.0.0" ,debug=True)