#example for -> elif
import sys
income = int(sys.argv[1])

if income < 0 :
    rate = 0.00
    print(rate)
elif income < 8925:
    rate = 0.10
    print(rate)
elif income < 36250:
    rate = 0.15
    print(rate)
elif income < 87850:
    rate = 0.23
    print(rate)