#!/usr/bin/python
import os
import subprocess
print('***********************************************')
print('********* Chuong trinh size directory *********')
print('***********************************************')
a = os.getcwd()
print('Directory in here: ' + a)
list_filename = os.listdir(a)
for name_file in list_filename:
    subprocess.call(["du","-hs",name_file])
