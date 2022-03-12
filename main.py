import os
from flask import Flask
from app.students.students import student_blueprint
from app.teachers.teachers import teacher_blueprint
import sqlalchemy
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['DB'] = sqlalchemy.create_engine(os.getenv('DB_HOST'))


app.register_blueprint(student_blueprint)
app.register_blueprint(teacher_blueprint)


@app.before_request
def interceptor():
    from flask import request, make_response

    authorization = request.headers.get('Authorization').split(
        ' ')[1] if request.headers.get('Authorization') else None

    if request.method != 'OPTIONS' and not authorization == os.getenv('AUTHORIZATION'):
        return make_response({'status': False, 'message': 'Unauthorized'}), 400
