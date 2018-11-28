import sys
from collections import defaultdict

# 	Given strings S and T, find the minimum contiguous sub-string, a window W, of S so that T 
# 	is a sub-sequence of W. If there is no such window in S that covers all characters in T, 
# 	return the empty string "". If there are multiple such minimum-length windows, return the 

# 	one with the left-most starting index. Example: S = "I have a friend that went to UPenn!" 
# 	T = "dtah", thus W = "d that"

def max_substring(s,t):
# assumes s, t are ASCII chars, solution is case insensitive
	# assumes t has repeated chars
	check = bytearray(128)
	count = 0
	# process t
	for c in t:		
		if check[helper_ord(c)] == 0:
			check[helper_ord(c)] = 1
			count += 1
	# construction vars
	final_start = -1
	final_length = 0		
	# processing vars
	unique = set()
	start = -1
	length = 0
	processing = False
	# process s
	for i in range (0,len(s)):
		val = helper_ord(s[i])
		# space case
		if val == 32: 
			if processing:
				length += 1
		elif check[val] == 1:
			if processing == False:
				unique.add(val)
				start = i
				length = 1
				processing = True
			else:
				length += 1
				unique.add(val)
			if len(unique) == count:
					# found valid set
					if length > final_length:
						final_start = start
						final_length = length
		else:
			# check processing set
			if processing:				
				unique = set()
				processing = False
	# construct return string
	ret = ""
	if final_start > -1:
		ret = counstruct_substring(s,final_start,final_length)
	return ret

def min_substring(s,t):
# assumes s, t are ASCII chars, solution is case insensitive
	# assumes t has repeated chars
	check = bytearray(128)
	count = 0
	# process t
	for c in t:		
		if check[helper_ord(c)] == 0:
			check[helper_ord(c)] = 1
			count += 1
	# construction vars
	final_start = -1
	final_length = sys.maxsize		
	# processing vars
	unique = set()
	freq = defaultdict(int)
	start = -1
	length = 0
	processing = False
	# process s
	i = 0
	while i < len(s):
		val = helper_ord(s[i])
		# space case
		if val == 32: 
			if processing:
				length += 1
		elif check[val] == 1:
			if processing == False:
				start = i
				length = 1
				processing = True
			else:
				length += 1
			unique.add(val)
			freq[val] += 1	
			if len(unique) == count:
				# found valid set
				# this loop trims characters off the front 
				# to see if a smaller valid substring can be created
				while len(unique) == count:
					# check if this can be returned
					if length < final_length:
						final_start = start
						final_length = length
					# trim first char and check
					first = helper_ord(s[start])
					freq[first] -= 1
					if freq[first] < 1:
						unique.remove(first)
					start += 1
					length -= 1

		else:
			# check processing set
			if processing:
				unique = set()
				freq = defaultdict(int)
				processing = False
		# manually iterate
		i+=1
	# construct return string
	ret = ""
	if final_start > -1:
		ret = counstruct_substring(s,final_start,final_length)
	return ret

# helper that lowercases chars
def helper_ord(c):
	return ord(c.lower())

# helper that constructs a substring from an substring, start index, and length
def counstruct_substring(string,start,length):
	if start+length-1 < len(string):
		ret = ""
		for i in range(start,start+length):
			ret += string[i]
		return ret
	else:
		return ""	

print('*** max function: ***')
print(max_substring('I have a friend that went to UPenn!','dtah'))
print(max_substring('I have a friend that went to UPenn dddttthhhaaattaaatthh!','dtah'))
print(max_substring('aardvarks are bad', 'vard'))
print(max_substring('aaaaaaa','a'))
print(max_substring('abd','bdgw'))
print(max_substring('a','a'))
print(max_substring('wdwa',''))
print(max_substring('','hduw'))
print()
print('*** min function: ***')
print(min_substring('I have a friend that went to UPenn!','dtah'))
print(min_substring('I have a friend that went to UPenn dddttthhhaaattaaatthh!','dtah'))
print(min_substring('feeaabcdate', 'abdc'))
print(min_substring('aardvarks are bad', 'vard'))
print(min_substring('abd','bdgw'))
print(min_substring('a','a'))
print(min_substring('aaaaaaa','a'))
print(min_substring('wdwa',''))
print(min_substring('','hduw'))


