import scipy
import pylab

nums = scipy.randn(100)

#Plot the data and a histogram of the data with 10 bins
pylab.plot(nums, 'ro')
pylab.savefig('randnplot.png')

pylab.cla() # clear the axes

pylab.hist(nums, 30) # 30 zone
pylab.savefig('randnhist.png')
