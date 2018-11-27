from numpy import array
from numpy import cov
x = array([1,2,3,4,5,6,7,8,9])
print(x)
y = array([1,2,3,4,5,6,7,8,9])
print(y)
Sigma = cov(x,y)
print(Sigma)


