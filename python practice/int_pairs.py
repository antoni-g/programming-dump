
# find pairs in the input collection of integers
# that have an exact difference
# inputs:
#		- list of integers
#		- integer absolute difference
# ouput:
#		- count of pairs

def find_pairs(nums,k):
	lookup = {}
    for i in nums:
        if i in lookup:
            lookup[i] = lookup[i] + 1
        else:
            lookup[i] = 1
    if k > 0:
        ret = set()
        for i in nums:
            if i + k in lookup:
                if not (i+k,i) in ret:
                    ret.add((i,i+k))
            if i - k in lookup:
                if not (i-k,i) in ret:
                    ret.add((i,i-k))
        return len(ret)
    elif k == 0:
        l = 0
        for i in lookup.keys():
            if lookup[i] > 1:
                l +=1
        return l
    else: 
        return 0

test = [1,2,3,4,5,6,7,8,9]
print(find_pairs(test,2))
test2 = [1,1,1,1,2,3,4,5,6,7,8,9]
print(find_pairs(test2,0))