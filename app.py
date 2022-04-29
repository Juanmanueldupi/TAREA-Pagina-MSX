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

libros=LeerLibreria()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/juegos')
def juegos():
    return render_template("juegos.html")



#port=os.environ["PORT"]
#app.run("0.0.0.0",int(port),debug=True)
app.run("0.0.0.0" ,debug=False)