class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_dup = ""
        #small = min(strs, key=len)
        for i in range(len(strs[0])):
            for n in strs:
                if i == len(n) or n[i] !=strs[0][i]:
                    return str_dup
            str_dup += strs[0][i]
                
        return str_dup