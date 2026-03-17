from flask import render_template, url_for, redirect
from FakePinterest import app, database, bcrypt
from FakePinterest.models import Usuario, Foto
from flask_login import login_required, login_user, logout_user, current_user
from FakePinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=formlogin.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, formlogin.senha.data):
            login_user(usuario, remember=True)
            return redirect(url_for("perfil", username=usuario.username))
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criar_conta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(formcriarconta.senha.data).decode("utf-8")
        usuario = Usuario(username=formcriarconta.username.data, email=formcriarconta.email.data, senha=senha)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", username=usuario.username))
    return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<username>")
@login_required
def perfil(username):
    return render_template("perfil.html", username=username)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))