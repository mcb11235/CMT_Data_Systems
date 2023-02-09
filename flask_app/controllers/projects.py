from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/projects')
def projects():
    projects = Project.get_all_posts()
    print(projects)
    return render_template('/projects.html', posts = projects)
@app.route('/add_project')
def add_project():
    return render_template('new_project.html')
@app.route('/publish_project', methods=['POST'])
def publish_project():
    if request.form['projectid'] == '' or request.form['project_manager'] == '':
        flash("All fields are required!")
        return redirect('/projects')
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
    Project.save_project(data)
    return redirect('/projects')
@app.route('/edit_project/<id>')
def edit_project(id):
    data = {
        'projectid': id
    }
    project_item = Project.get_one_by_id(data)
    return render_template('edit_project.html', item=project_item)
@app.route('/editproject', methods=['POST'])
def handle_edit_project():
    if request.form['projectid'] == '' or request.form['project_manager'] == '':
        flash("All fields are required!")
        return redirect('/projects')
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
    Project.update_project(data)
    return redirect('/projects')
@app.route('/delete_project', methods=['POST'])
def delete_project():
    if str(session['user']) != str(request.form['user_id']):
        flash("You Do Not Have Permission To Delet This")
        return redirect('/projects')
    data = {
        "id" : request.form['id']
    }
    Project.delete_recipe(data)
    return redirect('/projects')