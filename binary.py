#binary finder of a number
#Home work.
import sys
n = int(sys.argv[1])
bin = []
while n>0:
    remainder = n %2
    bin.insert(0,remainder)
    n //=2
for digit in (bin) :
    print(digit,end="")
