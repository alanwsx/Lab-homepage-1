# -*- coding: utf-8 -*-

from flask import render_template, jsonify, request, current_app
from . import app as app
from . import util

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/faculty')
def faculty():
    return render_template('faculty.html')

@app.route('/student')
def student():
    list = util.get_student_list()
    phd_list = filter(lambda dict: "博士" in dict[util.ACADEMIC_TITLE_KEY], list)
    master_list = filter(lambda dict: "硕士" in dict[util.ACADEMIC_TITLE_KEY], list)
    return render_template('student.html',
        person_list = list,
        phd_list = phd_list,
        master_list = master_list,
        NAME_KEY = util.NAME_KEY,
        ENGLISH_NAME_KEY = util.ENGLISH_NAME_KEY ,
        EMAIL_KEY = util.EMAIL_KEY,
        IMAGE_PATH_KEY=util.IMAGE_PATH_KEY)

@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/recruitment')
def recruitment():
    return render_template('recruitment.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
