#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from flask import Flask
import app
import os
from libs import pinyin



NAME_KEY='Name'
ENGLISH_NAME_KEY='English Name'
EMAIL_KEY='Email'
IMAGE_PATH_KEY='Image'


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
    r = {}
    name = dict[NAME_KEY]
    r[NAME_KEY] = name
    r[EMAIL_KEY] = dict['Email']
    postgraduate_image_dir = os.path.join(app.app.root_path, 'static/pic/postgraduate')
    image_path = os.path.join(postgraduate_image_dir,name+'.jpg')
    if os.path.exists(image_path):
        image_path = os.path.join('pic/postgraduate',name+'.jpg')
    else:
        image_path = 'pic/default_icon.jpg'
    r[IMAGE_PATH_KEY] = image_path

    r[ENGLISH_NAME_KEY] = dict[ENGLISH_NAME_KEY] if dict.get(ENGLISH_NAME_KEY) else convert_name_to_English(name)
    return r

person_list = None
def get_postgraduate_list():
    global person_list
    if person_list:
        return person_list
    csv_path = os.path.join(app.app.root_path, 'resource/postgraduate.csv')
    reader = csv.DictReader(file(csv_path, 'rb'))
    person_list = [format_person_info(dict) for dict in reader];
    return person_list
