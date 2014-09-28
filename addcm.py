#!/usr/bin/python
#coding=utf-8
import os

#coding:gbk
#path = '/Users/libinggen/Downloads/123/20140926/01'
path = '.'
from os.path import isdir, isfile
from os import listdir
parent = 0
def printdir(path):
    global parent
    if isdir(path):
        path2 = listdir(path)
        for i in path2:
            path3 = path+'/'+i
            if isdir(path3):
                #print '+' * parent, path3
                parent += 1
                printdir(path3)
            elif isfile(path3):
                #print '-' * parent, path3
       			portion = os.path.splitext(i)
       			#if portion[1] == ".h":
       			if portion[1] == '.h':
       				print path3
       				f = open(path3,'a')
       				f.write('\n123\n456\n')
       				f.close
       			elif portion[1] == '.m':
       				print path3
       				f = open(path3,'a')
       				f.write('\n123\n456\n')
       				f.close
            elif portion[1] == '.mm':
              print path3
              f = open(path3,'a')
              f.write('\n123\n456\n')
              f.close       		
    else:
        print path
printdir(path)