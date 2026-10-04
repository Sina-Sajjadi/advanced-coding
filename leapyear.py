import sys

year = int(sys.argv[1])

leap_year = (year % 4 == 0)
leap_year = leap_year and (year % 100 != 0)
leap_year = leap_year or (year % 400 == 0)

print(leap_year)