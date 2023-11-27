#polynomial  regression

import matplotlib.pyplot as abc
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
y=np.array([10,20,30,40,50,46,78,34,56,100,110,120,130])
abc.plot(x,y)
abc.show()


mymodel=np.poly1d(np.polyfit(x,y,3))
myline=np.linspace(1,13,100)
abc.scatter(x,y)
abc.plot(myline,mymodel(myline))
abc.show()