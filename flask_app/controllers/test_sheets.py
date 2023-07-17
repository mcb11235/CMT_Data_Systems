from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.schedule import Schedule
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
from flask_app.mongo_connection import connect_to_mongo
bcrypt = Bcrypt(app)
@app.route('/concrete_test_assignment/<id>', methods=['GET'])
def test_assignment(id):
    data = {
        'schedule_id': id
    }
    sample_id = str(id) + '-Cs1'
    schedule_item = Schedule.get_one_by_id(data)
    return render_template('/test_assignment.html', item = schedule_item, sample_id = sample_id)
@app.route('/assign_concrete_tests', methods=['POST'])
def assign_concrete_tests():
    mongo_instance = connect_to_mongo()
    print("Database Interface Established")
    concrete_samples = mongo_instance['concrete_samples']
    print("Database collection retreived")
    data = {
        'sample_id': request.form['sample_id'],
        'schedule_id': request.form['schedule_id']
    }
    assigned_tests = request.form.keys()
    for test in assigned_tests:
        data[test] = request.form[test]
    print("Attempting data injection")
    concrete_samples.insert_one(data)
    return redirect('/schedules')