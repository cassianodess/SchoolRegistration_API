from flask import current_app as app
from sqlalchemy import text

from models.student import Student


def list(name: str):
    with app.config['DB'].connect() as conn:

        query = ' SELECT * FROM students '

        if name:
            query += f" WHERE LOWER(name) LIKE '%{name}%' "
        
        response = conn.execute(text(query), name=name)

        response = response.fetchall()

        return [Student(id=student['id'], name=student['name'], course=student['course']).parse() for student in response] if response else dict()


def retrieve(id: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(
            text('SELECT * FROM students WHERE id = :id'), id=id)

        response = response.fetchone()

        return Student(
            id=response['id'],
            name=response['name'],
            course=response['course']
        ).parse() if response else dict()


def create(name: str, course: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(text("""
            INSERT INTO students
                (name, course)
            VALUES (:name, :course)
            RETURNING id, name, course """), name=name, course=course)
        response = response.fetchone()

        return Student(response['id'], response['name'], response['course']).parse()


def update(id: str, name: str, course: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(text("""
        UPDATE students
        SET name = :name, course = :course
        WHERE id = :id
        RETURNING id, name, course
        """), id=id, name=name, course=course)

        response = response.fetchone()

        return Student(
            id=response['id'],
            name=response['name'],
            course=response['course']
        ).parse() if response else dict()


def delete(id: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(text("""
        DELETE from students
        WHERE id = :id
        RETURNING id, name, course
        """), id=id)

        response = response.fetchone()

        return Student(
            id=response['id'],
            name=response['name'],
            course=response['course']
        ).parse() if response else dict()
