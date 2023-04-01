from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
schema_name = 'inspection_schema'
class Schedule:
    def __init__(self, data):
        self.schedule_id = data['schedule_id'],
        self.project_id = data['project_id'],
        self.field_representative = data['field_representative'],
        self.discipline = data['discipline'],
        self.start_time = data['start_time'],
        self.end_time = data['end_time'],
        self.date = data['date'],
        self.notes = data['notes']
    @classmethod
    def save_schedule(cls, data):
        query = "INSERT INTO schedules (schedule_id,project_id,field_representative,discipline,start_time,end_time,date,notes) VALUES (%(schedule_id)s,%(project_id)s,%(field_representative)s,%(discipline)s,%(start_time)s,%(end_time)s,%(date)s,%(notes)s);"
        return connectToMySQL(schema_name).query_db(query, data)
    @classmethod
    def update_schedule(cls, data):
        query = "UPDATE schedules SET field_representative=%(field_representative)s,discipline=%(discipline)s,start_time=%(start_time)s,end_time=%(end_time)s,date=%(date)s WHERE schedule_id=%(schedule_id)s;"
        return connectToMySQL(schema_name).query_db(query, data)    
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM schedules"
        schedules = []
        results = connectToMySQL(schema_name).query_db(query)
        for schedule in results:
            schedules.append(cls(schedule))
        return schedules
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM schedules WHERE schedule_id=%(schedule_id)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        print(results)
        return cls(results[0])
    @classmethod
    def delete_schedule(cls, data):
        query = "DELETE FROM schedules WHERE schedule_id=%(schedule_id)s"
        return connectToMySQL(schema_name).query_db(query, data)