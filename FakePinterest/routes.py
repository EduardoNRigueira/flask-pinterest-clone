from flask import render_template, url_for
from FakePinterest import app
from flask_login import login_required
from FakePinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<username>")
@login_required
def perfil(username):
    return render_template("perfil.html", username=username)