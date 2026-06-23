from flask import Flask, render_template, url_for, redirect
from flask_login import login_required, login_user, logout_user, current_user
from modocarreira import app, database
from modocarreira.forms import FormNovoJogador, FormTemporada
from modocarreira.models import Jogador, AnoJogador

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/carreiratreinador")
def treinador():
    return render_template("treinador.html")


@app.route("/carreirajogador")
def carreirajogador():
    return render_template("carreirajogador.html")


@app.route("/carreirajogador/novacarreirajogador", methods=["GET", "POST"])
def novojogador():
    form = FormNovoJogador()
    if form.validate_on_submit():
        jogador = Jogador(
            nome=form.nome.data,
            idade=form.idade.data,
            gols=0,
            assistencias=0,
            jogos=0,
            hathick=0,
            doublehathick=0,
            pentathick=0,
            hexathick=0,
            num_titulos=0)
        database.session.add(jogador)
        database.session.commit()
        return redirect(url_for("jogador", jogador=jogador.nome))
    return render_template("novacarreirajogador.html", form=form)


@app.route("/carreirajogador/carregarcarreirajogador/<jogador>/temporada", methods=["GET", "POST"])
def temporada(jogador):
    form = FormTemporada()
    dados_jogador = Jogador.query.filter_by(nome=jogador).first()
    if form.validate_on_submit():
        print("DEU CERTO ")
        temporada = AnoJogador(
            gols = form.gols.data,
            ano = form.ano.data,
            assistencias = form.assistencias.data,
            jogos = form.jogos.data,
            hathick = form.hathick.data,
            doublehathick = form.doublehathick.data,
            pentathick = form.pentathick.data,
            hexathick = form.hexathick.data,
            num_titulos = form.num_titulos.data
        )
        database.session.add(temporada)

        dados_jogador.gols += form.gols.data
        dados_jogador.assistencias += form.assistencias.data
        dados_jogador.jogos += form.jogos.data
        dados_jogador.hathick += form.hathick.data
        dados_jogador.doublehathick += form.doublehathick.data
        dados_jogador.pentathick += form.pentathick.data
        dados_jogador.hexathick += form.hexathick.data
        dados_jogador.num_titulos += form.num_titulos.data

        database.session.commit()

        return redirect(url_for("jogador", jogador=jogador))
    return render_template("temporada.html", form=form, jogador=dados_jogador)


@app.route("/carreirajogador/carregarcarreirajogador")
def carregarjogador():
    jogadores = Jogador.query.all()
    return render_template("carregarjogador.html", jogadores=jogadores)


@app.route("/carreirajogador/carregarcarreirajogador/<jogador>")
def jogador(jogador):
    jogador = Jogador.query.filter_by(nome=jogador).first()
    return render_template("jogador.html", jogador=jogador)