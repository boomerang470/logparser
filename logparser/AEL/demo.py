#!/usr/bin/env python

import sys
sys.path.append('../../')
from logparser.AEL import LogParser

input_dir     = '../../data/' # The input directory of log file
output_dir    = 'demo_result/' # The output directory of parsing results
log_file      = 'syslog' # The input log file name
log_format    = '<IP> <month> <date> <Timestamp> <num> <loc> <status>: <Content>' # HDFS log format
minEventCount = 2 # The minimum number of events in a bin
merge_percent = 0.5 # The percentage of different tokens
regex         = [r'^(\S+)\s+(\w{3}\s+\d{2})\s+(\d{2}:\d{2}:\d{2})\s+(\S+)\s+(\S+)\s+(.*)$'] # Regular expression list for optional preprocessing (default: [])

parser = LogParser(input_dir, output_dir, log_format, rex=regex,
                   minEventCount=minEventCount, merge_percent=merge_percent)
parser.parse(log_file)
