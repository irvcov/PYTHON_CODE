#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import shutil
import errno
    
class java_parser:

    def __init__(self):
	pass

    def java_to_javatest(self, java_path="", java_path_test=""):
	
	java_test_file = open(java_path_test,"w")
	java_test_file.write("\n\nimport org.testng.Assert;\n")
	java_test_file.write("import org.testng.annotations.Test;\n")
	java_test_file.write("import mockit.Mock;\n")
	java_test_file.write("import mockit.MockUp;\n")
	java_test_file.write("import mockit.Mocked;\n")
	java_test_file.write("import mockit.Verifications;\n\n")
	prev_line = ""

	with open(java_path,"r") as java_file:
            for line in java_file:
	        #print line
      
	        if( line=="{\n" or line == "}\n" ):
		    java_test_file.write(line);
	      
		else:
		    if(line.find(" class") != -1):
			pos = line.find("class")
			pos2 = line.find(" ", pos+6)
			pos3 = line.find("\n", pos+6)

			if(pos2 != -1):
			    classname = line[pos+6:pos2]
			elif (pos3 !=-1):
			    classname = line[pos+6:pos3]

			java_test_file.write("public class "+ classname+"Test\n")

		    elif(line=="    {\n" or line=="	{\n"):
		    
			if(prev_line.find("(") != -1): 
			    pos = prev_line.find("(")
			    pos2 = prev_line.rfind(" ",0, pos )
			    functionname = prev_line[pos2+1:pos]
			    #functionname[0:1].upper()
			    #print "pos:%s, pos2:%s, functionname:%s, prev_line:%s"%(pos,pos2,functionname,prev_line)
			    java_test_file.write("    @Test\n")
			    java_test_file.write("    public void test"+ functionname+"()\n")

			elif(prev_line.find(" class") != -1):
			    pos = prev_line.find("class")
			    pos2 = prev_line.find(" ", pos+6)
			    pos3 = prev_line.find("\n", pos+6)

			    if(pos2 != -1):
				classname = prev_line[pos+6:pos2]
			    elif (pos3 !=-1):
				classname = prev_line[pos+6:pos3]

			    java_test_file.write("class "+ classname+"Test\n")

			java_test_file.write(line);

		    elif(line == "    }\n" or line == "	}\n"):
			java_test_file.write(line+"\n");

		prev_line = line


    def java_to_javatest_per_folder(self, main_folder="", test_folder=""):
	list_main = os.listdir(main_folder)
	list_test = os.listdir(test_folder)

	for item in list_main:
	    itemTest = item.replace(".java","Test.java")
	    if itemTest not in list_test:
		if(item.find(".java") != -1):
		    print "make test: "+item +"    test: " + itemTest
		    self.java_to_javatest( main_folder+"/"+item, test_folder+"/"+itemTest)
	    else:
		print "skip item"

    def java_to_javatest_per_folder_tree(self, src_path=""):
	file_paths = []  # List which will store all of the full filepaths.
	file_dir = []

	dir_main = src_path + "/main"
	dir_test = src_path + "/test"

	# Walk the tree.
	for root, directories, files in os.walk(dir_main):	

	    #print "root: " + root
	    #print "--------------------------------------------"
	    
	    for direc in directories:
		build_tests = True
		folderpath_test = ""
		folderpath_main = os.path.join(root, direc)
		#folderpath_main = str(folderpath_main)
		folderpath_test = folderpath_main.replace("/main", "/test")
		#folderpath_test.replace("/main", "/test")
		
		#print "------------------------------------------------"
		print "main tree path, ",folderpath_main
		print "test tree path, ",folderpath_test
		#print "-------------------"

		list_main = os.listdir(folderpath_main)

		if os.path.exists(folderpath_test):
		  list_test = os.listdir(folderpath_test)
		else:
		  if(os.path.isdir(folderpath_main)):
		      print "---**This folder is in the main tree would you like to create the same folder in test tree?:\n " + folderpath_test
		      if (raw_input("'yes y: no n': ") == "y"): 
			os.makedirs(folderpath_test)
			build_tests = True
		      else:
			print "Folder Skipped"
			build_tests = False
		  #else:
		      #print "Is not Directory"

		#print "main tree,", list_main
		#print "test tree,", list_test
		print "---------------------------------------------------"

		if build_tests:
		    for item in list_main:
			itemTest = item.replace(".java","Test.java")
			if itemTest not in list_test:
			    if(item.find(".java") != -1):
				print "make test: "+item
				self.java_to_javatest( folderpath_main+"/"+item, folderpath_test+"/"+itemTest)
			else:
			    print "skip item"

    def compare_folder_project(self, src_path=""):

	file_paths = []  # List which will store all of the full filepaths.
	file_dir = []

	dir_main = src_path + "/main"
	dir_test = src_path + "/test"

	# Walk the tree.
	for root, directories, files in os.walk(dir_main):	

	    #print "root: " + root
	    #print "--------------------------------------------"

	    for direc in directories:

		folderpath_test = ""
		folderpath_main = os.path.join(root, direc)
		#folderpath_main = str(folderpath_main)
		folderpath_test = folderpath_main.replace("/main", "/test")
		#folderpath_test.replace("/main", "/test")
		
		#print "------------------------------------------------"
		#print "main tree path, ",folderpath_main
		#print "test tree path, ",folderpath_test
		#print "-------------------"

		list_main = os.listdir(folderpath_main)

		if os.path.exists(folderpath_test):
		  list_test = os.listdir(folderpath_test)
		else:
		  if(os.path.isdir(folderpath_test)):
		      print "hago folder: " + folderpath_test
		      

		print "main tree,", list_main
		print "test tree,", list_test
		print "------------------------------------------------"

		for item in list_main:
		    itemTest = item.replace(".java","Test.java")
		    if itemTest not in list_test:
			if(item.find(".java") != -1):
			    print "make test: "+item
			    
		    else:
			print "skip item"


jp = java_parser()
#print sys.argv
if len(sys.argv) == 1:
  print "this Script helps to create Unit Test files test.java frames function in order to save time in the unit test development"
  print "It takes 3 argument from bash:"
  print "First argument takes the function operation"
  print "Function (1): -It creates a unit test test.java file function frame from an specific .java file-"
  print "takes two extra arguments, .java file path which want to make the unit test and the test.java file path where you want to store the unit test"
  print "Function (2): -It creates a full folder unit test test.java file function frame from an specific main folder path-"
  print "takes two extra arguments, Folder file path which want to make the unit tests and the Folder file path where you want to store the unit test"
  print "Function (3): -It creates the unit tests test.java files for a full tree folder path, makin a mirrow test folder tree from main folder src tree-"
  print "take one extra argument,  tree folder src main path."
else:

  if sys.argv[1] == '1':
      #jp.java_to_javatest("/scratch/icovarru/gitsrc/emclas/platform/querylanguage/querylanguage-web-utils/src/main/java/oracle/sysman/emaas/platform/querylanguage/webutils/ServiceLookup.java",
	  #    "/scratch/icovarru/gitsrc/ServiceLookupTest.java")
      jp.java_to_javatest(sys.argv[2],sys.argv[3])
  elif sys.argv[1] == '2':
      jp.java_to_javatest_per_folder(sys.argv[2],sys.argv[3])
      #jp.java_to_javatest_per_folder("/scratch/icovarru/QLjiras/sprints/querylanguage_spring61/emclas/platform/querylanguage/querylanguage-web-utils/src/main/java/oracle/sysman/emaas/platform/querylanguage/webutils/metrics",
	  #		       "/scratch/icovarru/QLjiras/sprints/querylanguage_spring61/emclas/platform/querylanguage/querylanguage-web-utils/src/test/java/oracle/sysman/emaas/platform/querylanguage/webutils/metrics")
  elif sys.argv[1] == '3':
      jp.java_to_javatest_per_folder_tree(sys.argv[2])
      #jp.compare_folder_project("/scratch/icovarru/QLjiras/sprints/querylanguage_spring61/emclas/platform/querylanguage/querylanguage-web-utils/src/")


# ./m_unit_test.py 3 /scratch/icovarru/gitsrc/emclas/platform/querylanguage/querylanguage-web-utils/src
# ./m_unit_test.py 2 /scratch/icovarru/QLjiras/sprints/querylanguage_spring61/emclas/platform/querylanguage/querylanguage-web/src/main/java/oracle/sysman/emaas/platform/querylanguage/service/config /scratch/icovarru/QLjiras/sprints/querylanguage_spring61/emclas/platform/querylanguage/querylanguage-web/src/test/java/oracle/sysman/emaas/platform/querylanguage/service/config

