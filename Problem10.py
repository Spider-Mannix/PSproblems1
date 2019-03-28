#plot function of x, x^2 and 2^x in range [0,4]

#use pyplot
import matplotlib.pyplot as pl

#generate required range, which is also function y = x
x = range(0,5)

#function y = x^2
sq = [s*s for s in x]

#function y = 2x
twox = [2**a for a in x]

#plot each function using pyplot
pl.plot(x)
pl.plot(sq)
pl.plot(twox)

#show is used to display graph
pl.show()