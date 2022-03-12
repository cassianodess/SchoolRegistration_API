from flask import current_app as app
from sqlalchemy import text

from models.teacher import Teacher


def list(name: str):
    with app.config['DB'].connect() as conn:

        query = 'SELECT * FROM teachers'

        if name:
            query += f" WHERE LOWER(name) LIKE '%{name}%' "

        response = conn.execute(text(query), name=name)

        response = response.fetchall()

        return [Teacher(id=student['id'], name=student['name'], subject=student['subject']).parse() for student in response] if response else dict()


def retrieve(id: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(
            text('SELECT * FROM teachers WHERE id = :id'), id=id)

        response = response.fetchone()

        return Teacher(
            id=response['id'],
            name=response['name'],
            subject=response['subject']
        ).parse() if response else dict()


def create(name: str, subject: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(text("""
            INSERT INTO teachers
                (name, subject)
            VALUES (:name, :subject)
            RETURNING id, name, subject """), name=name, subject=subject)
        response = response.fetchone()

        return Teacher(response['id'], response['name'], response['subject']).parse()


def update(id: str, name: str, subject: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(text("""
        UPDATE teachers
        SET name = :name, subject = :subject
        WHERE id = :id
        RETURNING id, name, subject
        """), id=id, name=name, subject=subject)

        response = response.fetchone()

        return Teacher(
            id=response['id'],
            name=response['name'],
            subject=response['subject']
        ).parse() if response else dict()


def delete(id: str):
    with app.config['DB'].connect() as conn:
        response = conn.execute(text("""
        DELETE from teachers
        WHERE id = :id
        RETURNING id, name, subject
        """), id=id)

        response = response.fetchone()

        return Teacher(
            id=response['id'],
            name=response['name'],
            subject=response['subject']
        ).parse() if response else dict()
