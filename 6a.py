# import os.path
# import sys

# fname=input("enter the file name")
# if not os.path.isfile(fname):
#     print(fname,"doesnt exist")
#     sys.exit(0)

# infile=open(fname,'r')
# n=int(input("enter the number of lines to be read"))    
# linelist=infile.readlines()
# for i in range(n):
#     print(i+1,":",linelist[i])
# word=input("enter the word to count")
# cnt=0
# for line in linelist:
#     cnt+=line.count(word)

# print("the word"+word+"appears"+cnt+"times")    



import os.path
import sys

fname=input("enter the file name")
if not os.path.isfile(fname):
    print("file doesn'n exist")
    sys.exit(0)
infile=open(fname,'r')    
num=int(input("enter the number of lines to read"))
linelist=infile.readlines()
for i in range(num):
    print(i+1,':',linelist[i])
word=input("enter the word")
cnt=0
for line in linelist:
    cnt+=line.count(word)
print("the word",word,"appers",cnt,"times")