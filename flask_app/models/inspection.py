from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
schema_name = 'inspection_schema'
class Inspection:
    def __init__(self, data):
        self.inspection_date = data['inspection_date'],
        self.inspection_time = data['inspection_time'],
        self.inspection_latitude = data['inspection_latitude'],
        self.inspection_longitude = data['inspection_longitude'],
        self.inspection_disposition = data['inspection_disposition'],
        self.project_id = data['project_id']
            
    @classmethod
    def save_equipment(cls, data):
        query = "INSERT INTO equipment (users_id,serial_number,calibration_procedure,item,category,test_method,acquired_date,purchase_price,calibration_date,frequency,calibration_due,location,owner) VALUES ( %(users_id)s,%(serial_number)s , %(calibration_procedure)s, %(item)s, %(category)s, %(test_method)s, %(acquired_date)s,%(purchase_price)s,%(calibration_date)s,%(frequency)s,%(calibration_due)s,%(location)s,%(owner)s);"
        return connectToMySQL(schema_name).query_db(query, data)
    @classmethod
    def update_equipment(cls, data):
        query = "UPDATE equipment SET users_id=%(users_id)s,serial_number=%(serial_number)s,calibration_procedure=%(calibration_procedure)s,item=%(item)s,category=%(category)s,test_method=%(test_method)s,acquired_date=%(acquired_date)s,purchase_price=%(purchase_price)s,calibration_date=%(calibration_date)s,frequency=%(frequency)s,calibration_due=%(calibration_due)s,location=%(location)s,owner=%(owner)s WHERE id=%(id)s;"
        return connectToMySQL(schema_name).query_db(query, data)    
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM equipment JOIN users ON users_id=users.id "
        equipments = []
        results = connectToMySQL(schema_name).query_db(query)
        for equipment in results:
            equipments.append(cls(equipment))
        return equipments
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM equipment WHERE id=%(id)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        print(results)
        return cls(results[0])
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM equipment WHERE id=%(id)s"
        return connectToMySQL(schema_name).query_db(query, data)