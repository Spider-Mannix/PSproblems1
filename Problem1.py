#ask for number, create variables
x = int(input("Please input a postive integer:"))
ans = 0
i = 1

#from lecture video:
while i <= x:
  ans = ans + i
  i = i + 1

print(ans)

#if type(x)! = int or >=0 "not positive integer"