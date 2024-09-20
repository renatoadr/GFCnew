#!python3

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home')
def abrir_home():
    return render_template("home.html")

@app.route('/cad_empreend')
def abrir_cad_empreend():
    return render_template("cad_empreend.html")


app.run()