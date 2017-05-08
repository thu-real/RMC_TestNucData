#!/usr/bin/env python

import os

data_path = os.path.dirname(os.path.realpath(__file__))
xsdir_file = os.path.join(data_path, 'xsdir')

with open(xsdir_file, 'r') as f:
    xsdir_lines = f.readlines()
xsdir_lines[0] = 'DATAPATH=' + data_path + '\n'

with open(xsdir_file, 'w') as f:
    f.write(''.join(xsdir_lines))
