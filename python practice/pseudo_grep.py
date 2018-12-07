class Solution:
    def grep(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ret = []
        if len(needle) == 0:
            return ret
        s = set(needle)
        i = len(needle)-1
        iter = max(len(needle)-1, 1)
        while i < len(haystack):
            c = haystack[i]
            if c in s:
                # work backwards and check
                found = True
                for j in range(len(needle) - 1, -1, -1):      
                    if needle[j] != haystack[i-(len(needle)-j-1)]:
                        found = False
                if found:
                    ret.append(i - len(needle)+1)
                i+=1
            else:
                # skip ahead
                i += iter
        return ret

s = Solution()
check = s.grep('aaabbbccccbbccbbbbbcdef', 'bbb')
print( [3,14,15,16] == check)