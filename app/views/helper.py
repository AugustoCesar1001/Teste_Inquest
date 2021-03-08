import datetime
import jwt
from app import app
from .users import user_by_username
from werkzeug.security import check_password_hash
from flask import jsonify, request
from functools import wraps


def auth():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({'message': 'Não foi Possível Verificar', 'WWW-Authenticate': 'Basic auth="Login Required"'}), 401

    user = user_by_username(auth.username)
    if not user:
        return jsonify({'message': 'Usuário Não Encontrado', 'data': {}}), 401

    if user and check_password_hash(user.password, auth.password):
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.now() + datetime.timedelta(hours=12)},
                           app.config['SECRET_KEY'])
        return jsonify({'message': 'Token Validado com Sucesso', 'token': token.decode('UTF-8'),
                        'exp': datetime.datetime.now() + datetime.timedelta(hours=12)})

    return jsonify({'message': 'Não foi Possível Verificar', 'WWW-Authenticate': 'Basic auth="Login Required"'}), 401


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token está Faltando', 'data': {}}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = user_by_username(username=data['username'])
        except:
            return jsonify({'message': 'Token Inválido ou Expirado', 'data': {}}), 401
        return f(current_user, *args, **kwargs)
    return decorated