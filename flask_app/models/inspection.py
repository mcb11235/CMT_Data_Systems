from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
schema_name = 'inspection_schema'
class Inspection:
    def __init__(self, data):
        self.inspection_id = data['inspection_id'],
        self.inspection_date = data['inspection_date'],
        self.inspection_time = data['inspection_time'],
        self.inspection_latitude = data['inspection_latitude'],
        self.inspection_longitude = data['inspection_longitude'],
        self.inspection_disposition = data['inspection_disposition'],
        self.project_id = data['project_id']
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM inspections"
        inspections = []
        results = connectToMySQL(schema_name).query_db(query)
        for inspection in results:
            inspections.append(cls(inspection))
        return inspections
                
    @classmethod
    def save_inspection(cls, data):
        query = "INSERT INTO inspections (inspection_date,inspection_time,inspection_latitude,inspection_longitude,inspection_disposition,project_id) VALUES ( %(inspection_date)s,%(inspection_time)s,%(inspection_latitude)s,%(inspection_longitude)s,%(inspection_disposition)s,%(project_id)s);"
        return connectToMySQL(schema_name).query_db(query, data)
    @classmethod
    def update_inspection(cls, data):
        query = "UPDATE inspections SET inspection_date=%(inspection_date)s,inspection_time=%(inspection_time)s,inspection_latitude=%(inspection_latitude)s,inspection_longitude=%(inspection_longitude)s,inspection_disposition=%(inspection_disposition)s,project_id=%(project_id)s,acquired_date=%(acquired_date)s,purchase_price=%(purchase_price)s,calibration_date=%(calibration_date)s,frequency=%(frequency)s,calibration_due=%(calibration_due)s,location=%(location)s,owner=%(owner)s WHERE inspection_id=%(inspection_id)s;"
        return connectToMySQL(schema_name).query_db(query, data)    
    @classmethod
    def get_project_inspections(cls, data):
        query = "SELECT * FROM inspections WHERE project_id=%(project_id)s"
        inspections = []
        results = connectToMySQL(schema_name).query_db(query, data)
        for inspection in results:
            inspections.append(cls(inspection))
        return inspections
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM inspection WHERE inspection_id=%(inspection_id)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        return cls(results[0])
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM inspection WHERE inspection_id=%(inspection_id)s"
        return connectToMySQL(schema_name).query_db(query, data)