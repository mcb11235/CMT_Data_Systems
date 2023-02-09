from flask_app import app
from flask_app.models.user import User
from flask_app.controllers import users
from flask_app.models.post import Equipment
from flask_app.controllers import posts
from flask_app.controllers import dashboard
from flask_app.models.project import Project
from flask_app.controllers import projects
if __name__ == "__main__":
    app.run(debug=True)