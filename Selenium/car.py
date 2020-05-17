import os
import shutil
import csv
import pandas as pd
'''
#verify the path
path = input("Enter you directory path : ")

if os.path.exists(path):
    df_1 = os.listdir(path)
    for i in  df_1 :
        print(i)
else:
    print("please enter right path")

#copy content from one file to another
path = "D:\\WOLV"
print(list(os.walk(path)))


sfile = "abc.txt"
dfile  = "newfile.txt"


sfo = open("abc.txt",'r')
context = sfo.read()
sfo.close()


dfo = open("newfile.txt",'w')
dfo.write(context)
dfo.close()

#copy file from one folder to another

dest= r'D:\WOLV\Gamedata\WGame\Movies'
source = r'D:\WOLV\Gamedata\WGame\justcopy'

for root, subdirs, files in os.walk(source) :
    print('root',root)
    print('subdirs',subdirs)
    print('files',files)
    for file in files :
        path = os.path.join(root,file)
        shutil.copy(path,dest)


# working with CSV/excel

req_file = "D:\\learning\\business-operations-csv.csv"
fo = open(req_file,'r')
data = csv.reader(fo, delimiter="|")

for  each in data:
    print(each)

fo.close()


with open("D:\\learning\\business-operations-csv.csv",'r') as csv_file :
    csv_reader = csv.reader(csv_file)

    for line in csv_reader :
        print(line)

'''

data = pd.read_csv("D:\\learning\\business-operations-csv.csv",encoding='latin1' )
df = data.head()
print(df.columns)

print(df[['industry','size']])
print("\n\n\n")

print(df.iloc[0])
