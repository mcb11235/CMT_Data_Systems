from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.schedule import Schedule
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
from flask_app.mongo_connection import connect_to_mongo
bcrypt = Bcrypt(app)
@app.route('/field_sheet/<id>')
def field_sheet(id):
    data = {
        'schedule_id': id
    }
    schedule_item = Schedule.get_one_by_id(data)
    return render_template('/schedules.html', item = schedule_item)
@app.route('/publish_field_sheet')
def publish_field_sheet():
    mongo_instance = connect_to_mongo()
    print("Database Interface Established")
    field_sheets = mongo_instance['field_sheets']
    print("Database collection retreived")
    data = {
        'schedule_id': 'THIS IS A TEST OF THE DATABASE CONNECTION',
        'project_id': 'THIS WOULD COME FROM THE SYSTEM',
        'field_representative': 'THIS WOULD COME FROM THE SYSTEM',
        'start_time': '8:05',
        'end_time': '14:36',
        'notes': '''LOREM IPSUM ET CETERA ET CETERA ET TU BRUTUS'''
    }
    print("Attempting data injection")
    field_sheets.insert_one(data)
    return redirect('/schedules')
@app.route('/edit_field_sheet/<id>')
def edit_field_sheet(id):
    data = {
        'schedule_id': id
    }
    projects = Project.get_all_posts()
    schedule_item = Schedule.get_one_by_id(data)
    return render_template('edit_schedule.html', item=schedule_item, projects=projects)
@app.route('/editsheet', methods=['POST'])
def handle_edit_sheet():
    if request.form['date'] == '' or request.form['field_representative'] == '':
        flash("All fields are required!")
        return redirect('/schedules')
    data = {
        'schedule_id' : request.form['schedule_id'],
        'field_representative': request.form['field_representative'],
        'discipline': request.form['discipline'],
        'start_time': request.form['start_time'],
        'end_time': request.form['end_time'],
        'date': request.form['date']
    }
    Schedule.update_schedule(data)
    return redirect('/schedules')