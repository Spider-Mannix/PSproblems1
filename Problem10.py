#plot function of x, x^2 and 2^x in range [0,4]

#use pyplot

import matplotlib.pyplot as pl

x = range(0,5)
sq = [s*s for s in x]
twox = [2**a for a in x]

pl.plot(x)
#pl.show()

pl.plot(sq)
#pl.show()

pl.plot(twox)
pl.show()