from flask.json import jsonify
from app.views import companies
from app import app



# Route to Search All Companies
@app.route('/companies', methods=['GET'])
def get_all_companies():
    return companies.get_all_companies()

# Route to Search for an Entrepreneur's Companies
@app.route('/companies/<id>', methods=['GET'])
def get_all_user_bussinesses(id):
    return companies.get_all_user_businesses(id)

# Route to Search for Specific Company
@app.route('/company/<id>', methods=['GET'])
def get_company(id):
    return companies.get_company(id)

#Company Registration Route
@app.route('/companies/<id>', methods=['POST'])
def post_company(id):
    return companies.post_company(id)

# Update Business Route
@app.route('/companies/<id_company>', methods=['PUT'])
def update_company(id_company):
    return companies.update_company(id_company)

# Route to Delete Company
@app.route('/companies/<id_company>', methods=['DELETE'])
def delete_company(id_company):
    return companies.delete_company(id_company)