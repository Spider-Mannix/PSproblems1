#output every second word of an input string

#use whitespace as a separator? Then while loop?

x = input("Please enter a sentence:")

y = x.split()
z = y[::2]

for i in z:
    print(i)
