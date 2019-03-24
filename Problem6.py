#output every second word of an input string

#use whitespace as a separator? Then while loop?

x = input("Please enter a sentence:")

#split function separates string at whitespace
y = x.split()
#take every second component in list y
z = y[::2]

for i in z:
    print(i, end=" ")
#end command stops printing on new line