from flask_app import app
from flask_app.models.project import Project
from flask import render_template, redirect, request, session, flash
from flask_app.models.inspection import Inspection
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import base64
import staticmaps
import os
import io
from PIL import Image
def location_mapper(locations):
    context = staticmaps.Context()
    context.set_tile_provider(staticmaps.tile_provider_OSM)
    print(__file__)
    markers = []
    for location in locations:
        markers.append(staticmaps.create_latlng(location[0], location[1]))
    for marker in markers:
        context.add_object(staticmaps.Marker(marker, color=staticmaps.RED, size=12))
    image = context.render_pillow(800, 500)
    image.save('testmap.png')
    im = Image.open('testmap.png')
    data = io.BytesIO()
    im.save(data, "PNG")
    encoded_img_data = base64.b64encode(data.getvalue())    
    img_data = encoded_img_data.decode('utf-8') 
    return img_data

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
    # I DON'T KNOW WHY THIS CONDITIIONAL IS TRUE !!
    #if request.form['inspection_time'] == '' or request.form['inspection_latitude'] == '' or request.form['inspection_longitude'] == '' or request.form['inspection_disposition']:
    #    print(request.form['inspection_date'], request.form['inspection_time'], request.form['inspection_latitude'], request.form['inspection_longitude'], request.form['inspection_disposition'], request.form['project_id'])
    #    flash("All fields are required!")
    #    return redirect('/inspections')
    data = {
        'users_id': session['user'],
        'inspection_date': request.form['inspection_date'],
        'inspection_time': request.form['inspection_time'],
        'inspection_latitude': request.form['inspection_latitude'],
        'inspection_longitude': request.form['inspection_longitude'],
        'inspection_disposition': request.form['inspection_disposition'],
        'project_id': request.form['project_id']
    }
    Inspection.save_inspection(data)
    return redirect(f"/inspections/{data['project_id']}")
@app.route('/inspections/<project_id>')
def project_inspections(project_id):
    data = {
        'project_id': project_id
    }
    inspections = Inspection.get_project_inspections(data)
    # Location data must go into location_mapper as LIST of [latitude, longitude]
    locations = []
    for result in inspections:
        print(result.project_id)
        locations.append([float(result.inspection_latitude[0]), float(result.inspection_longitude[0])])
    map_data = location_mapper(locations)
    return render_template('/project_inspections.html', posts = inspections, img_data=map_data)
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