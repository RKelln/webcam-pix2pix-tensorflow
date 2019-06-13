#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: memo

params_list used to initialise a pyqtgraph.parametertree
http://www.pyqtgraph.org/documentation/parametertree/


this module will be populated and updated with parameters from params_list
"""

import glob

models = glob.glob('./models/*.json')

params_list = [
    {'name': 'Main', 'type': 'group', 'children': [
        {'name': 'quit', 'type': 'bool', 'value': False},
        {'name': 'verbose', 'type': 'bool', 'value': False},
        {'name': 'sleep_s', 'type': 'float', 'value': 0.1, 'limits': (0, 10)},
        {'name': 'liveshow', 'type': 'bool', 'value': True},
    ]},

    {'name': 'Capture', 'type': 'group', 'children': [
        {'name': 'enabled', 'type': 'bool', 'value': True},
        {'name': 'freeze', 'type': 'bool', 'value': False},
        {'name': 'sleep_s', 'type': 'float', 'value': 0.1, 'limits': (0, 10)},
        {'name': 'Init', 'type': 'group', 'children': [
            {'name': 'use_thread', 'type': 'bool', 'value': True},
            {'name': 'device_id', 'type': 'int', 'value': 0},
            {'name': 'width', 'type': 'int', 'value': 640},
            {'name': 'height', 'type': 'int', 'value': 480},
            {'name': 'fps', 'type': 'int', 'value': 15},
            {'name': 'reinitialise', 'type': 'bool', 'value': False},
        ]},
        {'name': 'Processing', 'type': 'group', 'children': [
            {'name': 'frame_diff', 'type': 'bool', 'value': False},
            {'name': 'flip_h', 'type': 'bool', 'value': False},
            {'name': 'flip_v', 'type': 'bool', 'value': False},
            {'name': 'grayscale', 'type': 'bool', 'value': False},
            {'name': 'pre_blur', 'type': 'int', 'value': 0},
            {'name': 'pre_median', 'type': 'int', 'value': 1},
            {'name': 'pre_thresh', 'type': 'int', 'value': 0},
            {'name': 'adaptive_thresh', 'type': 'bool', 'value': True},
            {'name': 'adaptive_thresh_block', 'type': 'int', 'value': 1, 'limits': (1, 100)},
            {'name': 'adaptive_thresh_c', 'type': 'int', 'value': 2},
            {'name': 'invert', 'type': 'bool', 'value': False},
            {'name': 'canny', 'type': 'bool', 'value': False},
            {'name': 'canny_t1', 'type': 'int', 'value': 1},
            {'name': 'canny_t2', 'type': 'int', 'value': 10},
            {'name': 'post_blur', 'type': 'int', 'value': 0},
            {'name': 'accum_w1', 'type': 'float', 'limits': (0, 1), 'value':0, 'step': 0.1},
            {'name': 'accum_w2', 'type': 'float', 'limits': (0, 1), 'value':0, 'step': 0.1},
            {'name': 'post_thresh', 'type': 'int', 'value': 0},
        ]},

    ]},

    {'name': 'Prediction', 'type': 'group', 'children': [
        {'name': 'enabled', 'type': 'bool', 'value': True},
        {'name': 'model', 'type': 'list', 'values': models, 'value': models[0]},
        {'name': 'pre_time_lerp', 'type': 'float', 'limits': (0, 1), 'value':0, 'step': 0.1},
        {'name': 'post_time_lerp', 'type': 'float', 'limits': (0, 1), 'value':0.5, 'step': 0.1},
    ]},

]
