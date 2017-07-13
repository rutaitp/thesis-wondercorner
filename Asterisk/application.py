#!/usr/bin/python

from asterisk.agi import *
import os, random

agi = AGI()

agi.verbose("python agi started")

#get the random file from the directory
filename = random.choice(os.listdir("/var/spool/asterisk/questions/loader/"))

#remove the extension
name_only = os.path.splitext(filename)[0]

file_path = "/var/spool/asterisk/questions/loader/" + name_only

agi.stream_file(file_path, escape_digits='', sample_offset=0)





