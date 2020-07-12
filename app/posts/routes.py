from flask import current_app, Blueprint, abort, jsonify, request, Response
from ..db import db
from .models import NodeModel
from .schemas import NodeSchema, NodeRequestSchema
from pprint import pprint

nodes = Blueprint('nodes', __name__)

@nodes.route('/', methods=['GET'])
def get():
    query = NodeModel.query.all()
    result = node_schema.dump(query, many=True)
    return jsonify(result)


@nodes.route('/<int:node_id>', methods=['GET'])
def get_by_id(node_id):
    query = NodeModel.query.filter_by(id=node_id).first()
    result = node_schema.dump(query)
    return jsonify(result)


@nodes.route('', methods=['POST'])
def post():
    errors = node_request.validate(request.get_json())
    if errors:
        abort(400, str(errors))
    query = NodeModel(request.json['address'], request.json['enabled'],
                 request.json['label'], request.json['password'], request.json['username'])
    db.session.add(query)
    db.session.commit()
    result = node_schema.dump(query)
    return jsonify(result), 201

