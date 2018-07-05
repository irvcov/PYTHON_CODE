#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import errno

def main():
    print "Start main!!"
    return 0


def get_filepaths(directory):
    """
    #This function will generate the file names in a directory 
    #tree by walking the tree either top-down or bottom-up. For each 
    #directory in the tree rooted at directory top (including top itself), 
    #it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.
    file_dir = []
    # Walk the tree.
    for root, directories, files in os.walk(directory):	
        for direc in directories:
            folderpath = os.path.join(root, direc)
            file_dir.append(folderpath)
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return (file_paths, file_dir)  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths, file_dir = get_filepaths("/home/icovarru/Documents/test_py")

print full_file_paths
print file_dir

def copy(src, dest):
    try:
        shutil.copytree(src, dest, ignore = shutil.ignore_patterns('*.py', '*.sh', 'specificfile.file'))
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)

#copy("/home/icovarru/Documents/test_py", "/home/icovarru/Documents/copy_test2")





