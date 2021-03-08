from app.models import companies
from flask import jsonify, request
from werkzeug.security import generate_password_hash
from app import db


from ..models.users import Users, user_schema, users_schema


# Specific User Search
def get_user(id):
    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({'message' : 'User Found Successfully', 'data': result}), 201
    return jsonify({'message' : 'User Not Localization', 'data': {}}), 404


# User Creation
def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    cpf_cnpj = request.json['cpf_cnpj']
    pass_hash = generate_password_hash(password)

    user = Users(username, pass_hash, name, cpf_cnpj)
    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'User Registration Success', 'data':result}), 201
    except:
        return jsonify({'message': 'Registration Failure'}), 500


# User Update
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    cpf_cnpj = request.json['cpf_cnpj']

    user = Users.query.get(id)
    if not user:
        return jsonify({'message': 'Non-Existent User', 'data':{}}), 404
    
    pass_hash = generate_password_hash(password)
    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.cpf_cnpj = cpf_cnpj
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message' : 'User Updated Successfully', 'data': result}), 201
    except:
        return jsonify({'message': 'Registration Failure'}), 500


# Delete User
def delete_user(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message':'Non-Existent User', 'data':{}}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'User Successfully Deleted', 'data':result}), 201
    except:
        return jsonify({'message': 'User Deletion Failed'}), 500 


# Search for Registered Users
def get_all():
    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({'message': 'Successful Users', 'data':result}), 201
    return jsonify({'message': 'There Are No Registered Users', 'data':{}}), 404


def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except:
        return None