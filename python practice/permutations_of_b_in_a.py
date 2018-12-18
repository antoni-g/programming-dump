# given two strings a and b, this algorithm finds 
# all permuations of b in a in O(N) time

# helper to compare two lists
# assume length will be the same
def comp(a,b):
	for i in range(0,len(a)):
		if a[i] != b[i]:
			return False
	return True

# returns a list of tuples of starting indicides
# and spliced substrings for permutations
def find_permutations(a,b):
	ret = []
	# assume an ASCII 256 char alphabet
	alpha = 256
	patL = len(b)
	strL = len(a)
	patArr = [0]*256
	strArr = [0]*256
	for i in range(patL):
		patArr[ord(b[i])]+=1
		strArr[ord(a[i])]+=1
	for i in range(patL,strL):
		if comp(patArr,strArr):
			ret.append((i-patL,a[i-patL:i]))
		strArr[ord(a[i])]+=1
		strArr[ord(a[i-patL])]-=1
	if comp(patArr,strArr):
		ret.append((strL-patL,a[strL-patL:strL]))
	return ret

print(find_permutations('abcdebdbabacbdbacbdecba','bca'))