#!/usr/bin/env python
# -*- coding: utf-8 -*-

import app
import getopt, sys

from flask import Flask

import sys
reload(sys)
sys.setdefaultencoding('utf8')


if __name__ == '__main__':
    port=5000
    opts, args = getopt.getopt(sys.argv[1:], '',["port="])
    for opt, arg in opts:
        if opt in ("--port"):
            port=int(arg)

    app.app.run(host='0.0.0.0',port=port,debug=True)

