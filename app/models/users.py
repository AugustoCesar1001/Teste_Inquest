import datetime

from sqlalchemy.orm import backref
from app import db, ma


"""Definição de Classe Tabela de Usuários"""
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    cpf_cnpj = db.Column(db.String(50), unique=True, nullable=False)
    companies = db.relationship('Companies', backref='owner')
    havings = db.relationship('Havings', backref='entrepreneur')
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, username, password, name, cpf_cnpj):
        self.username = username
        self.password = password
        self.name = name
        self.cpf_cnpj = cpf_cnpj


"""Definindo Schema"""
class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'password', 'cpf_cnpj', 'created_on')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)