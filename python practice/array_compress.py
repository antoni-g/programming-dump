import math

class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        new_len = 0
        if len(chars) > 0:
            compress_inx = 0
            curr_c = chars[0]
            curr_c_len = 1
            new_len = 0

            # subroute for outputting to array
            def output(chars,compress_inx,new_len,curr_c_len):
                chars[compress_inx] = curr_c
                compress_inx+=1
                new_len+=1
                if curr_c_len > 1:
                    # handle > 9
                    if curr_c_len > 9:
                        while curr_c_len > 9:
                            tens = int(math.log10(curr_c_len))
                            # get first digit
                            out = curr_c_len//(10**tens)                            
                            chars[compress_inx] = str(out)
                            compress_inx+=1
                            new_len+=1
                            curr_c_len %= 10**tens
                    # handle the rest
                    chars[compress_inx] = str(curr_c_len)
                    compress_inx+=1
                    new_len+=1
                return new_len,compress_inx

            for i in range(1,len(chars)):
                if chars[i] == curr_c:
                    curr_c_len+=1
                    if i == len(chars)-1:
                        res = output(chars,compress_inx,new_len,curr_c_len)
                        new_len = res[0]
                        compress_inx = res[1]
                else:
                    # output
                    res = output(chars,compress_inx,new_len,curr_c_len)
                    new_len = res[0]
                    compress_inx = res[1]
                    # update
                    curr_c = chars[i]
                    curr_c_len = 1
                    if i == len(chars)-1:
                        chars[compress_inx] = curr_c
                        new_len+=1
            
        return new_len

        

s = Solution()

l = []
print(s.compress(l))
print(l)

l = ['a']
print(s.compress(l))
print(l)

l = ['a','b']
print(s.compress(l))
print(l)

l = ['a','a']
print(s.compress(l))
print(l)

l = ['a','a','a']
print(s.compress(l))
print(l)

l = ['a' if i > 11 else 'b' for i in range(200)]
print(s.compress(l))
print(l)

l = ['a','a','a','a','b']
print(s.compress(l))
print(l)


l = ['a','a','a','a','a','c','b','b']
print(s.compress(l))
print(l)

l = ['a','a','b','b','b']
print(s.compress(l))
print(l)