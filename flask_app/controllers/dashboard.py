from datetime import date
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_app.models.inspection import Inspection
from flask_bcrypt import Bcrypt
from matplotlib.figure import Figure
import numpy as np
import base64
import staticmaps
import os
import io
from PIL import Image

bcrypt = Bcrypt(app)
@app.route('/dashboard')
def dashboard():
    id = session['user']
    data={'id': id}
    user = User.get_one(data)
    return render_template('dashboard.html', user=user)
@app.route('/chart')
def chart():
    fig = Figure()
    ax = fig.subplots()
    moisture_contents = (6, 8, 10, 12)
    densities = (110, 114, 116, 114)
    d,c,b,a = np.polyfit(moisture_contents, densities, deg=3)
    xseq = np.linspace(moisture_contents[0], moisture_contents[-1])
    ax.scatter(moisture_contents,densities)
    ax.plot(xseq, a+b*xseq+(c*xseq*xseq)+(d*xseq*xseq*xseq))
    buf = BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<img src='data:image/png;base64, {data}'/>"