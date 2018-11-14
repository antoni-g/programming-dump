import numpy

class Solution(object):
    def isPalindrome(self,s):
        l = len(s)
        mid = l//2
        for i in range(0,mid):
            if s[i] != s[l-i-1]:
            	return False
        return True
    
    def longestPalindrome(self, s):
        if s == '':
            return ''
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        self.memo = numpy.full((l,l),0)
        self.palindrome = s[0]
        self.recurse(s,0,l-1)
        return self.palindrome

    def recurse(self,s,i,j):
        self.memo[i][j] = 1
        temp =s[i:j+1]
        if (self.isPalindrome(temp)):
            print('found palindrome: ' + temp)
            self.palindrome = temp
            return
        else:
            if (len(temp)) <= len(self.palindrome):
                return # give up on this branch
            else:
                if self.memo[i][j-1] == 0:
                    self.recurse(s,i,j-1)
                if self.memo[i+1][j] == 0:
                    self.recurse(s,i+1,j)

        
run = Solution()
print(run.longestPalindrome('mmdewexxxxeeexxxxxxxfewfeeeeee'))