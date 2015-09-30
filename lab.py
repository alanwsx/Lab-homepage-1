#!/usr/bin/env python
# -*- coding: utf-8 -*-

import app
from flask import Flask

import sys
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == '__main__':
    app.app.run(host='0.0.0.0',debug=True)

