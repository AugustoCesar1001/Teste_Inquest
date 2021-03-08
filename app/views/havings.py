from flask import jsonify, request
from app import db


from ..models.havings import Havings, having_schema, havings_schema
from ..models.users import Users


# All to the Properties Of An Entrepreneur
def get_all_properties(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message':'Non-existent User', 'data':{}}), 404
    
    havings = Havings.query.filter_by(id_entrepreneur=id).all() #User.id =id
    if havings:
        result = havings_schema.dump(havings)
        return jsonify({'message' : 'Properties Found Successfully', 'data': result}), 201
    return jsonify({'message' : 'Properties Not Found Successfully', 'data': {}}), 404


# Items of a Particular Entrepreneur
def get_property(id, id_property):
    user = Users.query.get(id)
    having = Havings.query.get(id_property)
    if not user:
        return jsonify({'message':'Non-existent User', 'data':{}}), 404
    if not having:
        return jsonify({'message':'Nonexistent Property', 'data':{}}), 404
    
    result = having_schema.dump(having)
    return jsonify({'message' : 'Property Found Successfully', 'data': result}), 201
    

# Property Registration
def post_having(id):
    user = Users.query.get(id)
    if not user:
        return jsonify({'message':'Non-existent User', 'data':{}}), 404

    name = request.json['name']
    amount = request.json['amount']
    type = request.json['type']
    value = request.json['value']
    id_entrepreneur = id
    
    having = Havings(name, amount, type, value, id_entrepreneur)
    try:
        db.session.add(having)
        db.session.commit()
        result = having_schema.dump(having)
        return jsonify({'message': 'Successful Property Registration', 'data':result}), 201
    except:
        return jsonify({'message': 'Property Registration Failed', 'data':{}}), 500


# Update Properties
def update_property(id, id_property):
    user = Users.query.get(id)
    having = Havings.query.get(id_property)
    if not user:
        return jsonify({'message':'Non-existent User', 'data':{}}), 404
    if not having:
        return jsonify({'message':'Nonexistent Property', 'data':{}}), 404

    name = request.json['name']
    amount = request.json['amount']
    type = request.json['type']
    value = request.json['value']

    try:
        having.name = name
        having.amount = amount
        having.type = type
        having.value = value
        db.session.commit()
        result = having_schema.dump(having)
        return jsonify({'message' : 'User Updated Successfully', 'data': result}), 201
    except:
        return jsonify({'message': 'Registration Failure'}), 500


# Delete Property
def delete_property(id, id_property):
    user = Users.query.get(id)
    having = Havings.query.get(id_property)
    if not user:
        return jsonify({'message':'Non-existent User', 'data':{}}), 404
    if not having:
        return jsonify({'message':'Nonexistent Property', 'data':{}}), 404

    try:
        db.session.delete(having)
        db.session.commit()
        result = having_schema.dump(having)
        return jsonify({'message': 'Success in Deleting Property', 'data':result}), 201
    except:
        return jsonify({'message': 'Failed to Delete Property', 'data':result}), 500