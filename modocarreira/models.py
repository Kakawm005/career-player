#Criar as rotas do nosso site(links)
from modocarreira import database
from flask_login import UserMixin


class Jogador(database.Model, UserMixin):
    __tablename__ = "jogador"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    idade = database.Column(database.Date, nullable=False)
    gols = database.Column(database.Integer, nullable=False)
    assistencias = database.Column(database.Integer, nullable=False)
    jogos = database.Column(database.Integer, nullable=False)
    hathick = database.Column(database.Integer, nullable=False)
    doublehathick = database.Column(database.Integer, nullable=False)
    pentathick = database.Column(database.Integer, nullable=False)
    hexathick = database.Column(database.Integer, nullable=False)
    num_titulos = database.Column(database.Integer, nullable=False)
    titulos = database.relationship("AnoJogador", backref="jogador", lazy=True)

class AnoJogador(database.Model):
    __tablename__ = "anojogador"
    id = database.Column(database.Integer, primary_key=True)
    ano = database.Column(database.Integer, nullable=False)
    gols = database.Column(database.Integer, nullable=False)
    assistencias = database.Column(database.Integer, nullable=False)
    jogos = database.Column(database.Integer, nullable=False)
    hathick = database.Column(database.Integer, nullable=False)
    doublehathick = database.Column(database.Integer, nullable=False)
    pentathick = database.Column(database.Integer, nullable=False)
    hexathick = database.Column(database.Integer, nullable=False)
    num_titulos = database.Column(database.Integer, nullable=False)
    id_jogador = database.Column(database.Integer, database.ForeignKey("jogador.id"), nullable=False)
    titulos = database.relationship("TitulosJogador", backref="anojogador", lazy=True)


class TitulosJogador(database.Model):
    __tablename__ = "titulosjogador"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    id_anojogador = database.Column(database.Integer, database.ForeignKey("anojogador.id"), nullable=False)


class Treinador(database.Model, UserMixin):
    __tablename__ = "treinador"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    gols_times = database.Column(database.Integer, nullable=False)
    ass_times = database.Column(database.Integer, nullable=False)
    jogos_times = database.Column(database.Integer, nullable=False)
    num_titulos_times = database.Column(database.Integer, nullable=False)
    titulos_times = database.relationship("AnoTreinador", backref="treinador", lazy=True)


class AnoTreinador(database.Model):
    __tablename__ = "anotreinador"
    id = database.Column(database.Integer, primary_key=True)
    ano = database.Column(database.Integer, nullable=False)
    id_treinador = database.Column(database.Integer, database.ForeignKey("treinador.id"), nullable=False)
    titulos = database.relationship("TitulosTreinador", backref="anotreinador", lazy=True)


class TitulosTreinador(database.Model):
    __tablename__ = "titulostreinador"
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String, nullable=False)
    id_anotreinador = database.Column(database.Integer, database.ForeignKey("anotreinador.id"), nullable=False)
