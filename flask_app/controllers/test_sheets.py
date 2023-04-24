from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.schedule import Schedule
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
from flask_app.mongo_connection import connect_to_mongo
bcrypt = Bcrypt(app)
@app.route('/concrete_test_assignment/<id>')
def test_assignment(id):
    data = {
        'schedule_id': id
    }
    schedule_item = Schedule.get_one_by_id(data)
    return render_template('/test_assignment.html', item = schedule_item)