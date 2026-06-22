from modocarreira import app, database

from modocarreira.models import Jogador, AnoJogador, TitulosJogador, Treinador, AnoTreinador, TitulosTreinador
with app.app_context():
    database.create_all()