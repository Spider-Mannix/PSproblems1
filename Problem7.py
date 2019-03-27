#approximation of the square root of a floating point number

#Newtonian root from lecture video:

a = float(input("Approximate the square root of [a positive number]: "))
est = float(input("What do you think the answer is? "))

while abs((est**2)-a) > 0.01:
    est -= ((est**2)-a)/(2*est)

print(f"The square root of {a} is approximately {est}, within +/-0.01.")