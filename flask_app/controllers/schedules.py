from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.schedule import Schedule
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/schedules')
def schedules():
    schedules = Schedule.get_all_posts()
    print(schedules)
    return render_template('/schedules.html', posts = schedules)
@app.route('/add_schedule')
def add_schedule():
    return render_template('new_schedule.html')
@app.route('/publish_schedule', methods=['POST'])
def publish_schedule():
    if request.form['schedule_id'] == '' or request.form['project_manager'] == '':
        flash("All fields are required!")
        return redirect('/schedules')
    data = {
        'projectid': request.form['projectid'],
        'project_name': request.form['project_name'],
        'client_name': request.form['client_name'],
        'owner_name': request.form['owner_name'],
        'project_manager': request.form['project_manager'],
        'principal_engineer': request.form['principal_engineer'],
        'total_budget': request.form['total_budget'],
        'industry_sector': request.form['industry_sector']
    }
    Schedule.save_project(data)
    return redirect('/schedules')
@app.route('/edit_schedule/<id>')
def edit_schedule(id):
    data = {
        'schedule_id': id
    }
    project_item = Schedule.get_one_by_id(data)
    return render_template('edit_schedule.html', item=project_item)
@app.route('/editschedule', methods=['POST'])
def handle_edit_schedule():
    if request.form['projectid'] == '' or request.form['project_manager'] == '':
        flash("All fields are required!")
        return redirect('/schedules')
    data = {
        'projectid': request.form['projectid'],
        'project_name': request.form['project_name'],
        'client_name': request.form['client_name'],
        'owner_name': request.form['owner_name'],
        'project_manager': request.form['project_manager'],
        'principal_engineer': request.form['principal_engineer'],
        'total_budget': request.form['total_budget'],
        'industry_sector': request.form['industry_sector']
    }
    Schedule.update_project(data)
    return redirect('/schedules')
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