class Solution(object):
    def isPalindrome(self, x):
        y = str(x)
        z = len(y)-1
        for i, n in enumerate(y):
            if y[i] == y[z-i]:
                pass
            else:
                return False
                break
        return True