from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.schedule import Schedule
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
from flask_app.mongo_connection import connect_to_mongo
from datetime import datetime
from datetime import timedelta
bcrypt = Bcrypt(app)
@app.route('/concrete_redirect', methods=['POST'])
def concrete_redirect():
    schedule_id = request.form['schedule_id']
    return redirect(f'/field_sheet/{schedule_id}')
@app.route('/field_sheet/<id>')
def field_sheet(id):
    # Check if field sheet is already in database
    mongo_instance = connect_to_mongo()
    field_sheets = mongo_instance['field_sheets']
    # If there is already a document for the schedule_id, return a page with the data
    if (field_sheets.find_one({'schedule_id': id})) != None:
        mongo_instance = connect_to_mongo()
        field_sheets = mongo_instance['field_sheets']
        field_sheet_data = field_sheets.find_one({'schedule_id': id})
        return render_template('/field_sheet_data.html', data = field_sheet_data)
    # If there is not a document for the schedule_id, return the form for entering data
    else:
        data = {"schedule_id": id}
        schedule_item = Schedule.get_one_by_id(data) 
        return render_template('field_sheet_form.html', schedule_item = schedule_item)    
@app.route('/publish_field_sheet', methods=['POST'])
def publish_field_sheet():
    mongo_instance = connect_to_mongo()
    print("Database Interface Established")
    field_sheets = mongo_instance['field_sheets']
    print("Database collection retreived")
    time_format = '%H:%M'
    duration = datetime.strptime(request.form['end_time'], time_format)-datetime.strptime(request.form['start_time'], time_format)  
    data = {
        'schedule_id': request.form['schedule_id'],
        'project_id': request.form['project_id'],
        'field_representative': request.form['field_representative'],
        'discipline': request.form['discipline'],
        'field_activity_date': request.form['field_activity_date'],
        'start_time': request.form['start_time'],
        'end_time': request.form['end_time'],
        'duration' : duration/timedelta(hours=1), 
        'general_location': request.form['general_location']
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
def handle_edit_field_sheet():
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
