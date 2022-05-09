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
    listacategorias=[]
    for juego in msxjuegos:
        if juego["categoria"] not in listacategorias:
            listacategorias.append(juego["categoria"])
    return render_template("juegos.html", listacategorias=listacategorias)

@app.route('/juegos',methods=["POST"])
def listajuegos():
    libreria = []
    buscadorjuegos=request.form['juego']
    for juego in msxjuegos:
        nombre = str(juego.get("nombre"))
        if nombre.startswith(str(buscadorjuegos)):
            dict={"nombre":juego.get("nombre"),"desarrollador":juego.get("desarrollador"),"id":juego.get("id")}
            libreria.append(dict)            
    return render_template("listajuegos.html", msxjuegos=libreria,buscadorjuegos=buscadorjuegos)

@app.route('/juego/<id>')
def juego(id):
    for juego in msxjuegos:
        if juego.get("id") == int(id):
            return render_template("juego.html",juego=juego)
    abort(404)



#port=os.environ["PORT"]
#app.run("0.0.0.0",int(port),debug=True)
app.run("0.0.0.0" ,debug=True)