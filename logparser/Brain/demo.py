#!/usr/bin/env python

import sys
sys.path.append('../../')
from logparser.Brain import LogParser

dataset    = 'HDFS'
input_dir  = '../../data/' # The input directory of log file
output_dir = 'demo_result/'  # The output directory of parsing results
log_file   = 'syslog'  # The input log file name
log_format = '<IP> <month> <date> <Timestamp> <num> <loc> <status>: <Content>'  # HDFS log format
# Regular expression list for optional preprocessing (default: [])
regex      = [
	r'^(\S+)\s+(\w{3}\s+\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\S+)\s+(\S+)\s+(.*)$'
]
threshold  = 2  # Similarity threshold
delimeter  = []  # Depth of all leaf nodes

parser = LogParser(logname=dataset, log_format=log_format, indir=input_dir, 
                   outdir=output_dir, threshold=threshold, delimeter=delimeter, rex=regex)
parser.parse(log_file)
