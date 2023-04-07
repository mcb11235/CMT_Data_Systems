from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.schedule import Schedule
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/schedules')
def schedules():
    schedules = Schedule.get_all_posts()
    print(schedules)
    return render_template('/schedules.html', posts = schedules)
@app.route('/add_schedule')
def add_schedule():
    projects = Project.get_all_posts()
    return render_template('new_schedule.html', projects = projects)
@app.route('/publish_schedule', methods=['POST'])
def publish_schedule():
    if request.form['field_representative'] == '' or request.form['date'] == '':
        flash("All fields are required!")
        return redirect('/add_schedule')
    data = {
        'schedule_id': request.form['schedule_id'],
        'project_id': request.form['project_id'],
        'field_representative': request.form['field_representative'],
        'discipline': request.form['discipline'],
        'start_time': request.form['start_time'],
        'end_time': request.form['end_time'],
        'date': request.form['date'],
        'notes': request.form['notes']
    }
    Schedule.save_schedule(data)
    return redirect('/schedules')
@app.route('/edit_schedule/<id>')
def edit_schedule(id):
    data = {
        'schedule_id': id
    }
    projects = Project.get_all_posts()
    schedule_item = Schedule.get_one_by_id(data)
    return render_template('edit_schedule.html', item=schedule_item, projects=projects)
@app.route('/editschedule', methods=['POST'])
def handle_edit_schedule():
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
@app.route('/schedules/<id>')
def show_schedule(id):
    data = {
        'schedule_id': id
    }
    schedule_item = Schedule.get_one_by_id(data)
    return render_template('show_schedule.html', item=schedule_item)
@app.route('/receive_field_report', methods=['POST'])
def receive_field_report():
    print(type(request.form))
    if request.form['field_report_received']:
        sample_status = "true"
    return redirect(f"/schedules/{request.form['schedule_id']}")
@app.route('/delete_schedule', methods=['POST'])
def delete_schedule():
    if str(session['user']) != str(request.form['user_id']):
        flash("You Do Not Have Permission To Delet This")
        return redirect('/schedules')
    data = {
        "id" : request.form['id']
    }
    Schedule.delete_recipe(data)
    return redirect('/schedules')