#output every second line from a text file

#use command line arguments
import sys 

#read text file then split by new line
txt = sys.argv
fls = open(txt[1],'r')
x23 = fls.read()
lines = x23.split('\n')

#every second line
vnm = lines[::2]

for i in vnm:
    print(i)