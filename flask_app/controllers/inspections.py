from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.inspection import Inspection
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
@app.route('/equipment')
def equipment_dashboard():
    equipments = Equipment.get_all_posts()
    return render_template('/equipment.html', posts = equipments)
@app.route('/add_equipment')
def add_equipment():
    return render_template('new_equipment.html')
@app.route('/publish', methods=['POST'])
def publish():
    if request.form['serial_number'] == '' or request.form['item'] == '' or request.form['calibration_date'] == '' or request.form['calibration_due'] == '':
        flash("All fields are required!")
        return redirect('/equipment')
    data = {
        'users_id': session['user'],
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
    Equipment.save_equipment(data)
    return redirect('/equipment')
@app.route('/edit_equipment/<id>')
def edit(id):
    data = {
        'id': id
    }
    equipment_item = Equipment.get_one_by_id(data)
    return render_template('edit_equipment.html', item=equipment_item)
@app.route('/edit', methods=['POST'])
def handle_edit():
    if request.form['serial_number'] == '' or request.form['item'] == '' or request.form['calibration_date'] == '' or request.form['calibration_due'] == '':
        flash("All fields are required!")
        return redirect('/equipment')
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
    Equipment.update_equipment(data)
    return redirect('/equipment')
@app.route('/delete', methods=['POST'])
def delete_post():
    if str(session['user']) != str(request.form['user_id']):
        flash("You Do Not Have Permission To Delet This")
        return redirect('/equipment')
    data = {
        "id" : request.form['id']
    }
    Equipment.delete_recipe(data)
    return redirect('/equipment')