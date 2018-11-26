class Solution(object):
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        oddLength = 1
        evenLength = -1
        oddStart = 0
        evenStart = -1
        for i in range(0,len(s)):
            # consider as center of odd palindrome
            tempLength = 1
            left = i-1
            right = i+1
            tempCenter = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    tempLength+=2
                    if tempLength > oddLength:
                        oddLength = tempLength
                        oddStart = tempCenter
                    left -= 1
                    right += 1
                else:
                    break
            # consider as center of even palindrome
            if not i == len(s)-1:
                tempLength = 0
                left = i
                right = i+1
                while left >= 0 and right < len(s):
                    if s[left] == s[right]:
                        tempLength+=2
                        if tempLength > evenLength:
                            evenLength = tempLength
                            evenStart = tempCenter
                        left -= 1
                        right += 1
                    else:
                        break
        # construct string to return
        temp = ""
        if oddLength >= evenLength:
            temp = s[oddStart]
            for i in range(1, oddLength//2 + 1):
                temp = s[oddStart-i] + temp + s[oddStart+i]
        else:
            for i in range(0,evenLength//2):
                temp = s[evenStart-i] + temp + s[evenStart+1+i]
        return temp
        
run = Solution()
print(run.longestPalindrome('cebbbbed'))