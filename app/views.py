from flask import render_template, jsonify, request, current_app
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/recruitment')
def recruitment():
    return render_template('recruitment.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
