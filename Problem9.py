#output every second line from a text file

#read text file then split like problem 6 but with new line operator e.g. split(/n)
txt = str(input("File name to open?"))
lines = open(txt,'r')

print(lines.read())