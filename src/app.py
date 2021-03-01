import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
   
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }

    return jsonify(response_body), 200

@app.route('/members', methods=['POST'])
def add_members():

    # this is how you can use the Family datastructure by calling its methods
    member_new = request.get_json()
    if isinstance(member_new, dict):
        members = jackson_family.add_members(member_new)
        response_body = {
            "family": members
    }
        return jsonify(response_body), 200
    else:
        return jsonify({"msg":"400 Bad Request"}), 400

@app.route('/members', methods=['DELETE'])
def delete_members(id=None):
    eliminado = jackson_family.delete_member(id)
    if eliminado:
        # response_body = {
        #     "family": members
        # }
        return jsonify({"msg":"El miembro se ha removido"}), 200
    else:
        return jsonify({"msg":"id no se reconoce"}), 404

@app.route('/members/<int:id>', methods=['PUT'])
def update_members(id=None):
    updatemem = request.get_json()
    modificado = jackson_family.update_member(id, updatemem)
    if modificado:
        return jsonify({"msg":"El miembro se ha actualizado"}),200
    else: 
        
        return jsonify({"msg":"400 Bad Request"}), 400


@app.route('/members/<int:id>', methods=['GET'])
def get_member_by(id):
    member = jackson_family.get_member(id)
    if member != None:
        # response_body = {
        #     "family": member
        # }
        return jsonify(member), 200
    else: 
        
        return jsonify({"msg":"El id es inexistente"}), 404



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
