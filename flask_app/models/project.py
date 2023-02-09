from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash
from flask_bcrypt import Bcrypt
schema_name = 'inspection_schema'
class Project:
    def __init__(self, data):
        self.projectid = data['projectid'],
        self.project_name = data['project_name'],
        self.client_name = data['client_name'],
        self.owner_name = data['owner_name'],
        self.project_manager = data['project_manager'],
        self.principal_engineer = data['principal_engineer'],
        self.total_budget = data['total_budget'],
        self.industry_sector = data['industry_sector']
    @classmethod
    def save_project(cls, data):
        query = "INSERT INTO projects (projectid,project_name,client_name,owner_name,project_manager,principal_engineer,total_budget,industry_sector) VALUES (%(projectid)s,%(project_name)s,%(client_name)s,%(owner_name)s,%(project_manager)s,%(principal_engineer)s,%(total_budget)s,%(industry_sector)s);"
        return connectToMySQL(schema_name).query_db(query, data)
    @classmethod
    def update_project(cls, data):
        query = "UPDATE projects SET project_name=%(project_name)s,client_name=%(client_name)s,owner_name=%(owner_name)s,project_manager=%(project_manager)s,principal_engineer=%(principal_engineer)s,total_budget=%(total_budget)s,industry_sector=%(industry_sector)s WHERE projectid=%(projectid)s;"
        return connectToMySQL(schema_name).query_db(query, data)    
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM projects"
        projects = []
        results = connectToMySQL(schema_name).query_db(query)
        for project in results:
            projects.append(cls(project))
        return projects
    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM projects WHERE projectid=%(projectid)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        print(results)
        return cls(results[0])
    @classmethod
    def get_by_user(cls, data):
        query = "SELECT * FROM projects WHERE project_manager=%(project_manager)s"
        results = connectToMySQL(schema_name).query_db(query, data)
        return cls(results[0])
    @classmethod
    def delete_recipe(cls, data):
        query = "DELETE FROM projects WHERE id=%(id)s"
        return connectToMySQL(schema_name).query_db(query, data)