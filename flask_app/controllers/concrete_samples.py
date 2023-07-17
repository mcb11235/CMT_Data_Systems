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
    field_sheets_collection = mongo_instance['field_sheets']
    concrete_samples = []
    for sample in concrete_samples_collection.find():
        data = {}
        field_sheet = field_sheets_collection.find_one({"schedule_id": sample['schedule_id']})
        tests = list(sample.keys())
        tests.pop(0)
        tests.pop(0)
        tests.pop(0)
        tests.pop(-1)
        print(tests)
        # TESTS LIST NEEDS TO BE PROCESSED BEFORE DISPLAY
        processed_tests = []
        for test in tests:
            processed = str(test.replace('_', ' '))
            processed = processed.title()
            processed_tests.append(processed)
        data['project_id'] = field_sheet['project_id']
        data['schedule_id'] = field_sheet['schedule_id']
        data['sample_id'] = sample['sample_id']
        data['sample_date'] = field_sheet['field_activity_date']
        data['general_location'] = field_sheet['general_location']
        data['tests'] = processed_tests
        concrete_samples.append(data)
    return render_template('concrete_samples.html', samples=concrete_samples)
