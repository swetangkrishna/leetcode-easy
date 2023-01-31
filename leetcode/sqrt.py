import math
class Solution(object):
    def mySqrt(self, x):
        if x ==1:
            return 1
        else:
            l = 0
            r = x
            while l+1<r:
                m = (l+r)/2
                if m*m>x:
                    r = m
                if m*m<x:
                    l = m
                if m*m==x:
                    return m
            return(int((l+r)/2))




