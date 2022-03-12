import json
from flask import Blueprint, make_response, request
from repository import teachers as teacher_repo
teacher_blueprint = Blueprint(
    'teacher_blueprint', __name__, url_prefix='/api/teachers')


@teacher_blueprint.route('', methods=['GET'])
def list():
    try:
        name = request.args.get('name')

        teachers = teacher_repo.list(name=name)

        return make_response({'message': 'success', 'data': teachers}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@teacher_blueprint.route('/<id>', methods=['GET'])
def retrieve(id):
    try:
        teacher = teacher_repo.retrieve(id=id)

        if not teacher:
            raise Exception('Teacher not found')

        return make_response({'message': 'success', 'data': teacher}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@teacher_blueprint.route('', methods=['POST'])
def create():
    try:
        body = json.loads(request.data)

        teacher = teacher_repo.create(
            name=body['name'], subject=body['subject'])

        return make_response({'message': 'success', 'data': teacher}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@teacher_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    try:
        body = json.loads(request.data)

        teacher = teacher_repo.update(
            id=id, name=body['name'], subject=body['subject'])

        if not teacher:
            raise Exception('Teacher not found')

        return make_response({'message': 'success', 'data': teacher}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@teacher_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    try:

        teacher = teacher_repo.delete(id=id)

        if not teacher:
            raise Exception('Teacher not found')

        return make_response({'message': 'success', 'data': teacher}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400
