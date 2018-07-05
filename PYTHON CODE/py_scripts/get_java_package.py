#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil

print "q show"

def get_java_pkg(src_path="", out_path=""):

    out = open(out_path+"/output_java_package.txt","w")
    # Walk the tree.
    for root, directories, files in os.walk(src_path):	

	#print "root: " + root
	#print "--------------------------------------------"

	for direc in directories:
	    folderpath = os.path.join(root, direc)
	    print folderpath

	    files = os.listdir(folderpath)
	    

	    for file in files:
		full_file = os.path.join(root, direc, file)
		ini = full_file.find("oracle")
		output =  full_file[ini:-5].replace('/','.')
		out.write('<class name="'+output+'"/>\n')
		print output
		#print file

get_java_pkg("/scratch/icovarru/QLjiras/sprints/querylanguage_spring61/emclas/platform/querylanguage/querylanguage-common-utils/src/test","/scratch/icovarru/QLjiras/py_scripts")