from flask.json import jsonify
from app.views import helper
from app.views import users
from app import app



''' User Information '''
@app.route('/v1', methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify({'message':f'Hello {current_user.name}'})


''' Specific User Search Route '''
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return users.get_user(id)


''' User's Search Route '''
@app.route('/users', methods=['GET'])
def get_users():
    return users.get_all()


''' User Creation Route '''
@app.route('/users', methods=['POST'])
def post_user():
    return users.post_user()


''' User Update Route '''
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    return users.update_user(id)


''' User Exclusion Route '''
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return users.delete_user(id)


''' User Authentication Route'''
@app.route('/auth', methods=['POST'])
def authenticate():
    return helper.auth()