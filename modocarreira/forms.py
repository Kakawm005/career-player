# Criar os formularios do nosso site
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DateField
from wtforms.validators import DataRequired, ValidationError 
from modocarreira.models import Jogador

class FormNovoJogador(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    idade = DateField("Data de nascimento", validators=[DataRequired(),])
    botao_confirmacao = SubmitField("Criar Carreira Jogador")

def validate_nome(self, nome):
    usuario = Jogador.query.filter_by(nome=nome.data).first()
    if usuario:
        return ValidationError("Já existe uma Carreira com esse Jogador'")
    
class FormTemporada(FlaskForm):
    gols = IntegerField("Gols", validators=[DataRequired()])
    assistencias = IntegerField("Assistencias", validators=[DataRequired()])
    jogos = IntegerField("Jogos", validators=[DataRequired()])
    hathick = IntegerField("Hathicks", validators=[DataRequired()])
    doublehathick = IntegerField("Doublehathick", validators=[DataRequired()])
    pentathick = IntegerField("Pentathick", validators=[DataRequired()])
    hexathick = IntegerField("Hexathick", validators=[DataRequired()])
    num_titulos = IntegerField("Numero de Titulos", validators=[DataRequired()])
    botao_confirmacao = SubmitField("Confirmar Temporada")