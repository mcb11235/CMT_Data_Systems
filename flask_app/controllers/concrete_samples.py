from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.schedule import Schedule
from flask_app.models.project import Project
from flask_bcrypt import Bcrypt
from flask_app.mongo_connection import connect_to_mongo
from datetime import datetime
from datetime import timedelta
bcrypt = Bcrypt(app)
@app.route('/concrete', methods=['GET'])
def display_concrete_samples():
    mongo_instance = connect_to_mongo()
    concrete_samples_collection = mongo_instance['concrete_samples']
    concrete_samples = []
    for sample in concrete_samples_collection.find():
        concrete_samples.append(sample)
    return redirect(f'/field_sheet/{schedule_id}')
