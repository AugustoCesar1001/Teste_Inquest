import datetime
from app import db, ma


"""Definição de Classe Tabela de Companhias"""
class Companies(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(30), unique=True, nullable=False)
    cpf_cnpj = db.Column(db.String(14), unique=True, nullable=False)
    id_owners = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, company_name, cpf_cnpj, id_owners):
        self.company_name = company_name
        self.cpf_cnpj = cpf_cnpj
        self.id_owners = id_owners


"""Definindo Schema"""
class CompaniesSchema(ma.Schema):
    class Meta:
        fields = ('id', 'company_name', 'cpf_cnpj', 'id_owners', 'created_on')


company_schema = CompaniesSchema()
companies_schema = CompaniesSchema(many=True)