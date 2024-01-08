#!/usr/bin/env python

import sys
sys.path.append('../../')
from logparser.NuLog import LogParser

input_dir = '../../data/loghub_2k/Windows/' # The input directory of log file
output_dir = 'demo_result/'  # The output directory of parsing results
log_file = 'syslog.log'  # The input log file name
log_format = '<IP> <month> <date> <Timestamp> <num> <loc> <status>: <Content>'  # HDFS log format
# Regular expression list for optional preprocessing (default: [])
regex = [r'^(\S+)\s+(\w{3}\s+\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\S+)\s+(\S+)\s+(.*)$']
filters = "(\s+blk_)|(:)|(\s)"
k = 15
nr_epochs = 5 # Number of epochs to run
num_samples = 0

parser = LogParser(log_format=log_format, indir=input_dir, outdir=output_dir, filters=filters, k=k)
parser.parse(log_file, nr_epochs=nr_epochs, num_samples=num_samples)
