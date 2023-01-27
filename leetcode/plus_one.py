class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dup = ''

        for i in range(len(digits)):
            dup += ''+ str(digits[i])
        dup2 = int(dup)
        dup2 = dup2 + 1
        dup = str(dup2)
        dig = []
        for i in range(len(dup)):
            dig.append(int(dup[i]))
        return dig