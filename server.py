from flask_app import app
from flask_app import mongo_connection
from flask_app.models.user import User
from flask_app.controllers import users
from flask_app.models.inspection import Inspection
from flask_app.controllers import inspections
from flask_app.controllers import dashboard
from flask_app.models.project import Project
from flask_app.controllers import projects
from flask_app.models.schedule import Schedule
from flask_app.controllers import schedules
from flask_app.controllers import field_sheets
from flask_app.controllers import test_sheets
from flask_app.controllers import concrete_samples
if __name__ == "__main__":
    app.run(debug=True)
    