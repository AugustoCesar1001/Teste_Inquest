import datetime
from app import db, ma


"""Definição de Classe Tabela de Bens"""
class Havings(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(60), nullable=False)
    amount = db.Column(db.Integer, unique=True, nullable=False)
    type = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.Float, unique=True, nullable=False)
    id_entrepreneur = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, name, amount, type, value, id_entrepreneur):
        self.name = name
        self.amount = amount
        self.type = type
        self.value = value
        self.id_entrepreneur = id_entrepreneur


"""Definindo Schema"""
class HavingsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'amount', 'type', 'value', 'id_entrepreneur', 'created_on')


having_schema = HavingsSchema()
havings_schema = HavingsSchema(many=True)