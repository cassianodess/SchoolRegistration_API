import json
from flask import Blueprint, make_response, request
from repository import students as student_repo
student_blueprint = Blueprint(
    'student_blueprint', __name__, url_prefix='/api/students')


@student_blueprint.route('', methods=['GET'])
def list():
    try:
        name = request.args.get('name')

        students = student_repo.list(name=name)

        return make_response({'message': 'success', 'data': students}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@student_blueprint.route('/<id>', methods=['GET'])
def retrieve(id):
    try:
        student = student_repo.retrieve(id=id)

        if not student:
            raise Exception('Student not found')

        return make_response({'message': 'success', 'data': student}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@student_blueprint.route('', methods=['POST'])
def create():
    try:
        body = json.loads(request.data)

        student = student_repo.create(name=body['name'], course=body['course'])

        return make_response({'message': 'success', 'data': student}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@student_blueprint.route('/<id>', methods=['PUT'])
def update(id):
    try:
        body = json.loads(request.data)

        student = student_repo.update(
            id=id, name=body['name'], course=body['course'])

        if not student:
            raise Exception('User not found')

        return make_response({'message': 'success', 'data': student}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400


@student_blueprint.route('/<id>', methods=['DELETE'])
def delete(id):
    try:

        student = student_repo.delete(id=id)

        if not student:
            raise Exception('Student not found')

        return make_response({'message': 'success', 'data': student}), 200

    except Exception as e:
        return make_response({'message': 'error', 'error': f'{e}'}), 400
