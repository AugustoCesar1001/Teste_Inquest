from app.models.havings import Havings
from flask import json, jsonify, request
from app import db


from ..models.companies import Companies, company_schema, companies_schema
from ..models.users import Users


# All Registered Companies
def get_all_companies():
    companies = Companies.query.all()
    if companies:
        result = companies_schema.dump(companies)
        return jsonify({'message' : 'Companies Found Successfully', 'data': result}), 201
    return jsonify({'message' : 'No registered companies', 'data':{}}), 404


# Enterprises Of An Entrepreneur
def get_all_user_businesses(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'Non-existent User', 'data':{}}), 404 
    companies = Companies.query.filter_by(id_owners=id).all()
    if companies:
        result = companies_schema.dump(companies)
        return jsonify({'message' : 'Companies Found Successfully', 'data':result}), 201
    return jsonify({'message': 'Companies not found', 'data':{}}), 404


# Specific Company Search
def get_company(id):
    companie = Companies.query.get(id)
    if companie:
        result = company_schema.dump(companie)
        return jsonify({'message' : 'Localized Company', 'data':result}), 201
    return jsonify({'message' : 'Company Not Found', 'data':{}}), 404


# Company Registration
def post_company(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'Non-existent User', 'data':{}}), 404
    
    company_name = request.json['company_name']
    cpf_cnpj = request.json['cpf_cnpj']
    id_owers = id
    
    companies = Companies(company_name, cpf_cnpj, id_owers)
    try:
        db.session.add(companies)
        db.session.commit()
        result = company_schema.dump(companies)
        return jsonify({'message' : 'Company Successfully Registered', 'data': result}), 201
    except:
        return jsonify({'message' : 'Failed to Register Company', 'data': {}}), 500


# Company Updated Successfully
def update_company(id_company):
    company = Companies.query.get(id_company)
    if not company:
        return jsonify({'message': 'Company Not Found', 'data':{}}), 404

    company_name = request.json['company_name']
    cpf_cnpj = request.json['cpf_cnpj']
    try:
        company.company_name = company_name
        company.cpf_cnpj = cpf_cnpj
        db.session.commit()
        result = company_schema.dump(company)
        return jsonify({'message': 'Company Updated Successfully', 'data':result}), 201
    except:
        return jsonify({'message' : 'Failed to Update Company', 'data':{}}), 500


# Successfully Deleted Company
def delete_company(id_company):
    company = Companies.query.get(id_company)
    if not company:
        return jsonify({'message': 'Company Not Found', 'data':{}}), 404

    try:
        db.session.delete(company)
        db.session.commit()
        result = company_schema.dump(company)
        return jsonify({'message' : 'Company Successfully Deleted', 'data':result}), 201
    except:
        return jsonify({'message' : 'Failed To Delete Company', 'data':{}}), 500