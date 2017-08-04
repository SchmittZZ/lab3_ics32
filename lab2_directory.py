from pathlib import Path
from pathlib import *
import os
import csv 
from sys import exit
count_csv = 0
count_all = 0
csv_file = []
def look_for_txt(p: 'path'):
    '''search the files whose name end in csv'''    
    pa = Path(p).glob('*.txt')
    for i in pa:
        global count_csv
        global csv_file
        csv_file.append(i)
        count_csv+=1
    return



##
##def create_directory(p:'path'):
##    '''create a directory if the directory does not exist.'''
##    pa = Path(p)
##    if pa.exists() ==False:
##        Path(pa).mkdir(parents=True, exist_ok=True)
##    return pa

def count_all_file(p:'path'):
    pa = Path(p).glob('*')
    for i in pa:
        global count_all
        count_all += 1
    return
    

inp=''
def interface_direc():
    '''interface that asking the user to type the directory'''
    global inp
    inp = input("What directory do you want to put? If finished, type 'done' to stop the program.")
    if (Path(inp).exists()==False and inp.lower()!='done'):
        inp2=input("The Path does not exist, do you want to create one? (yes/no)")
        if inp2.lower()=='yes':
            create_directory(inp)
        if inp2.lower()=='no':
            interface_direc()
    if inp.lower() =='done':
        print('The program is finished.')
        exit()
    else:
        print("The path is valid")
        look_for_csv(inp)
        count_all_file(inp)
        print(count_csv)
        print(count_all)
    


