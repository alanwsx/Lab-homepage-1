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

@app.route('/postgraduate')
def postgraduate():
    list = util.get_postgraduate_list()
    return render_template('postgraduate.html',
        person_list = list,
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
