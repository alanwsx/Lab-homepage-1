#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from flask import Flask
import app
import os
from libs import pinyin



NAME_KEY='Name'
ACADEMIC_TITLE_KEY='Academic Title'
ENGLISH_NAME_KEY='English Name'
EMAIL_KEY='Email'
IMAGE_PATH_KEY='Image'
URL_KEY="URL"


converter = pinyin.Converter()
def convert_name_to_English(name):
    name = name.decode('utf-8')
    first_name = name[0]
    second_name = ''.join(name[1:])
    #convert to PinYin
    first_name = converter.convert(first_name).capitalize()
    # second_name = converter.convert(second_name).capitalize().replace(' ', '')

    second_name = [converter.convert(n).capitalize() for n in name[1:]]
    second_name = '-'.join(second_name)

    English_name = second_name + ' ' + first_name
    return English_name


def format_person_info(dict):
    name = dict[NAME_KEY]
    student_image_dir = os.path.join(app.app.root_path, 'static/pic/student')
    image_path = os.path.join(student_image_dir,name+'.jpg')
    print image_path
    if os.path.exists(image_path):
        image_path = os.path.join('pic/student',name+'.jpg')
    else:
        image_path = 'pic/default_icon.jpg'
    dict[IMAGE_PATH_KEY] = image_path

    if not dict.get(ENGLISH_NAME_KEY):
        dict[ENGLISH_NAME_KEY] = convert_name_to_English(name)

    return dict

person_list = None
def get_student_list():
    global person_list
    if person_list:
        return person_list
    csv_path = os.path.join(app.app.root_path, 'resource/student.csv')
    reader = csv.DictReader(file(csv_path, 'rb'))
    person_list = [format_person_info(dict) for dict in reader];
    return person_list
