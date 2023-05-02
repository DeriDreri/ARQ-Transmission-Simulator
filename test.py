import numpy


tab = [1,2,3,4]
tab2 = [5,6,7,8]
tab = numpy.array(tab)
tab2 = numpy.array(tab2)
tab2 = numpy.append(tab, tab2)
print(tab2)