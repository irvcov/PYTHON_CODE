#!/usr/bin/env python
# -*- coding: utf-8 -*-
#---- Dev: Irving Covarrubias -icovarru- irving.covarrubias@oracle.com

import subprocess
import sys

class del_char:

    def __init__(self, path="/scratch/icovarru/QLjiras/sprints/emclas", file_type="json"):
	self.path = path
	self.file_type = "*."+file_type
	self.out = None

    def find_files(self):
	p = subprocess.Popen(["find", self.path, "-name", self.file_type], stdout=subprocess.PIPE)
	d = subprocess.Popen(["xargs", "grep","-Pl", "\r"], stdin=p.stdout, stdout=subprocess.PIPE)
	(out,err) = d.communicate()
	self.out = out.split("\n")
	
	for o in self.out:
	    print o
	print "You have: %s, %s files with \\r"%(len(self.out)-1, self.file_type.replace("*." , ""))
	

    def clear_char(self):

	con = raw_input("Do you want to delete the character \\r for all the previous files? y/yes:n ")
	
	if con == "y" or con == "yes":
	    for o in self.out:
		print o
		subprocess.Popen(["dos2unix", o], stdout=subprocess.PIPE)
	else:
	    print "Doing nothing."

if len(sys.argv) == 1:
    print "this Script helps to delete the character \\r and ^M, resolving the issue for the JIRA EMCLAS-10482 "
    print "In order to run the script you have to give 2 arguments, first is the path where ou want to delete the characters"
    print "and the scond one the file type"
    print "example: $./del_char_emclas_10482.py /scratch/icovarru/QLjiras/sprints/emclas json"
else:
  
    #delc = del_char()
    #delc.find_files()
    if len(sys.argv) == 3:
	if sys.argv[1] != None and sys.argv[2] != None:   #./del_char_emclas_10482.py /scratch/icovarru/QLjiras/sprints/emclas json
      
	  delc = del_char(sys.argv[1], sys.argv[2])
	  delc.find_files()
	  delc.clear_char()
    else:
	print "This function takes just 2 arguments example:$./del_char_emclas_10482.py /scratch/icovarru/QLjiras/sprints/emclas json "