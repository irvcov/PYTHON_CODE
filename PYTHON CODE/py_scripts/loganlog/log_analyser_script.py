#!/usr/bin/env python
# -*- coding: utf-8 -*-
#./log_analyser_script.py 1 "/scratch/icovarru/QLjiras/py_scripts/loganlog/logan.log"

import sys
import os
import shutil
import errno
import collections

def isSimilarWord(word1, word2, similitud_range=0.85, coef1=1, coef2=1, coef3=0):
    print "word1: "+word1+" word2: "+word2

    range1 = 0.0
    range2 = 0.0
    similitud_coef = 0.0

    #word1
    for i,c in enumerate(word1):
	charc = ord(c) - coef3   #coef4 takes type of character
	range1 =+ float(charc*charc* (i+1) * coef1)    #coef1 takes positions of character
    len_wd1 = len(word1)
    range1 = range1 / float(len_wd1*len_wd1 * coef2)   #coef2 takes longitud of character

    #word2
    for i,c in enumerate(word2):
	charc = ord(c) - coef3
	range2 =+ float(charc*charc* (i+1) * coef1)
    len_wd2 = len(word2)
    range2 = range2 / float(len_wd2*len_wd2 * coef2)

    if(range2 > range1):
	similitud_coef = float(range1/range2)
    else:
	similitud_coef = float(range2/range1)

    print "word1: "+str(range1)+" word2: "+str(range2) + " Similitud: " +str(similitud_coef*100) +"%"
    #print " "
    
    if(similitud_coef > similitud_range):
	return True
    else:
	return False


class word_dict:

    def __init__(self):
	self.wd_dict = dict()
	self.list_categorys = []
	self.list_categorys.append("warning")
	self.list_categorys.append("possible error")
	self.list_categorys.append("error")
	self.default_words()

    def add_word(self, word, category):
	self.wd_dict[word] = self.list_categorys[category]

    def add_category(self, category):
	self.list_categorys.append(category)

    def contain_word(self, word):
	return self.wd_dict.has_key(word)

    def default_words(self):
	self.wd_dict["java"] = self.list_categorys[0]
	self.wd_dict["exception"] = self.list_categorys[1]
	self.wd_dict["error"] = self.list_categorys[2]

    def getWords(self):
	return self.wd_dict.keys()

    def getWord(self, key):
	return self.wd_dict.get(key)

#global word_dic 

class Read_log:

    def __init__(self, path):
	self.path = path
	#global word_dic 
	self.word_dic = word_dict()

    def get_lines(self):
	with open(self.path,"r") as read_file:
	    #self.read_file = read_file
	    for line in read_file:
		yield line

    def process_log(self):
	num_line = 0
	lines_list = []
	result_dict = dict()
	#result_dict = collections.OrderedDict(sorted(d.items()))

	for line in self.get_lines():
	    #print line
	    lines_list.append(line)
	    split_line = line.split(" ")
	    #print split_line
	    words_find = self.procress_split_line(split_line)
	    
	    if len(words_find) > 0:
		result_dict[num_line] = words_find

	    num_line += 1

	print "Number of lines read: "+str(num_line)

	result_dict = collections.OrderedDict(sorted(result_dict.items(), reverse=True))
	return (lines_list, result_dict)
	    
    def procress_split_line(self, split_line):
	words_find = []
	for word in split_line:
	    grower_wd = ""
	    grower_wd2 = ""
	    word2 = word
	    for lttr in word2.lower():
		
		if lttr.isalpha():
		    grower_wd += lttr
		    if self.word_dic.contain_word(grower_wd):
			words_find.append(self.word_dic.getWord(grower_wd))
			words_find.append(word)
		else:
		    grower_wd2 += lttr
		    if self.word_dic.contain_word(grower_wd2):
			words_find.append(self.word_dic.getWord(grower_wd2))
			words_find.append(word)

	return words_find

    def procress_split_line2(self, split_line):
	words_find = []
	for word in split_line:
	    print word

	return words_find

class main:
    def __init__(self, path):
	self.readlog = Read_log(path)
	(self.lines_list, self.result_dict) = self.readlog.process_log()

    def see_latest_event(self, event_type, numberOflines):
	category = self.readlog.word_dic.list_categorys[event_type]
	
	for nline in self.result_dict.keys():
	    #print nline
	    #print self.result_dict.get(nline)
	    listevent = self.result_dict.get(nline)
	    if category in listevent:
		print "------------------------"
		print listevent
		for i in range(nline-numberOflines,nline+numberOflines):
		    print self.lines_list[i]
		print "------------------------"
		break

    def see_event_onebyone(self, event_type, numberOflines):
	category = self.readlog.word_dic.list_categorys[event_type]
	
	for nline in self.result_dict.keys():
	    #print nline
	    #print self.result_dict.get(nline)
	    listevent = self.result_dict.get(nline)
	    if category in listevent:
		print "------------------------"
		print listevent
		for i in range(nline-numberOflines,nline+numberOflines):
		    print self.lines_list[i]
		print "------------------------"
		exit = raw_input("exit? pres y: ")
		if exit == 'y':
		    break

    def see_results(self):
	print self.result_dict

#path = "/scratch/icovarru/QLjiras/py_scripts/loganlog/logan.log"
    
if len(sys.argv) == 1:
  print "this Script helps to create "
  print isSimilarWord("[ERROR]","ERROR")
  print isSimilarWord("exception","exceptions")
  print isSimilarWord("exception","exceptionsssssss")
  print isSimilarWord("error","exceptions")
  print isSimilarWord("this is a phrase","this phrase is")
  print isSimilarWord("exception","except")
  print isSimilarWord("muydiferente","aesto")
  print isSimilarWord("This is a similar text than the other","these are a similar texts than others")

else:

  if sys.argv[1] == '1':
      m = main(sys.argv[2])
      print "** Welcome to the log analyser script **"
      print " -Press 1 to see results"
      print " -Press 2 to see last event"
      print " -Press 3 to see event one by one"

      while(True):

	action = raw_input("Action: ")

	if action == '1':
	  m.see_results()

	if action == '2':
	  typeEvent = raw_input("Type of event: ") #2
	  m.see_latest_event(int(typeEvent),3)

	if action == '3':
	  typeEvent = raw_input("Type of event: ")
	  m.see_event_onebyone(int(typeEvent),3)

	action = raw_input("Exit? pres y: ")
	if(action):
	    break




