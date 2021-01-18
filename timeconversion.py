import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    h, m, sec = map(int, s[:-2].split(':'))
    p = s[-2:]
    h = h % 12 + (p.upper() == 'PM') * 12
    return(('%02d:%02d:%02d') % (h, m, sec))

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')

