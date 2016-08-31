from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import division

import os


root = os.path.abspath(os.path.dirname(__file__))
DATA_NAME = 'data'


def file_location(file_name):
    return os.path.join(root, DATA_NAME, file_name)
