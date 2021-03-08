from flask.json import jsonify
from app.views import havings
from app import app



''' Route to Get All Properties '''
@app.route('/having/<id>', methods=['GET'])
def get_all_property(id):
    return havings.get_all_properties(id)


''' Route to Get Property '''
@app.route('/having/<id>/<id_property>', methods=['GET'])
def get_property(id, id_property):
    return havings.get_property(id, id_property)


''' Property to Register Route '''
@app.route('/having/<id>', methods=['POST'])
def post_property(id):
    return havings.post_having(id)


''' Route to Update Property '''
@app.route('/having/<id>/<id_property>', methods=['PUT'])
def update_property(id, id_property):
    return havings.update_property(id, id_property)


''' Route to Delete Property '''
@app.route('/having/<id>/<id_property>', methods=['DELETE'])
def delete_property(id, id_property):
    return havings.delete_property(id, id_property)