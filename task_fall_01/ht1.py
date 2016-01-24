import sys
import numpy as np

if len(sys.argv) >= 2:
	if int(sys.argv[1]) > 0:
		n = int(sys.argv[1])
	else:
		n = 100
else:
	n = 100

mu, sigma = 0 ,1 

s = np.random.normal(mu, sigma, n)

def mad(s):
	med = np.mean(s)
	return np.mean(np.abs(s - med))

print n
print "Mean average deviation:", mad(s)
print "Standart deviation:", np.std(s)