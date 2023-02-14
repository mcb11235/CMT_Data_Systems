from flask_app import app
from flask_app.models.project import Project
from flask import render_template, redirect, request, session, flash
from flask_app.models.inspection import Inspection
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/inspections')
def inspections_dashboard():
    inspections = Inspection.get_all_posts()
    return render_template('/inspection.html', posts = inspections)
@app.route('/add_inspection')
def add_inspection():
    projects = Project.get_all_posts()
    return render_template('new_inspection.html', projects=projects)
@app.route('/publish_inspection', methods=['POST'])
def publish_inspection():
    if request.form['inspection_date'] == '' or request.form['inspection_time'] == '' or request.form['inspection_latitude'] == '' or request.form['inspection_longitude'] == '' or request.form['inspection_disposition']:
        flash("All fields are required!")
        return redirect('/inspection')
    data = {
        'users_id': session['user'],
        'inspection_date': request.form['serial_number'],
        'inspection_time': request.form['calibration_procedure'],
        'inspection_latitude': request.form['test_method'],
        'inspection_longitude': request.form['item'],
        'inspection_disposition': request.form['category'],
        'project_id': request.form['acquired_date']
    }
    Inspection.save_equipment(data)
    return redirect(f'/inspection/{data.project_id}')
@app.route('/edit_equipment/<id>')
def edit(id):
    data = {
        'id': id
    }
    equipment_item = Inspection.get_one_by_id(data)
    return render_template('edit_equipment.html', item=equipment_item)
@app.route('/edit', methods=['POST'])
def handle_edit():
    if request.form['serial_number'] == '' or request.form['item'] == '' or request.form['calibration_date'] == '' or request.form['calibration_due'] == '':
        flash("All fields are required!")
        return redirect('/inspection')
    data = {
        'users_id': session['user'],
        'id': request.form['id'],
        'serial_number': request.form['serial_number'],
        'calibration_procedure': request.form['calibration_procedure'],
        'test_method': request.form['test_method'],
        'item': request.form['item'],
        'category': request.form['category'],
        'acquired_date': request.form['acquired_date'],
        'purchase_price': request.form['purchase_price'],
        'calibration_date': request.form['calibration_date'],
        'frequency': request.form['frequency'],
        'calibration_due': request.form['calibration_due'],
        'location': request.form['location'],
        'owner': request.form['owner']
    }
    Inspection.update_equipment(data)
    return redirect('/inspection')
@app.route('/delete', methods=['POST'])
def delete_post():
    if str(session['user']) != str(request.form['user_id']):
        flash("You Do Not Have Permission To Delet This")
        return redirect('/inspection')
    data = {
        "id" : request.form['id']
    }
    Inspection.delete_recipe(data)
    return redirect('/inspection')