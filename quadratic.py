import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

delta =  (b**2) - (4.0*a*c)

if delta >= 0 :
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

print(str(a) + 'x^2 ' + '+ ' + str(b) + 'x ' + '+ ' + str(c))
print('root = ' + str(x1) + ' and ' + str(x2))