# 	Given strings S and T, find the minimum contiguous sub-string, a window W, of S so that T 
# 	is a sub-sequence of W. If there is no such window in S that covers all characters in T, 
# 	return the empty string "". If there are multiple such minimum-length windows, return the 

# 	one with the left-most starting index. Example: S = "I have a friend that went to UPenn!" 
# 	T = "dtah", thus W = "d that"

def substring(s,t):
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
		else:
			# check processing set
			if processing:
				if len(unique) == count:
					# found valid set
					if start + length - 1 > final_length:
						final_start = start
						final_length = length
				unique = set()
				processing = False
	# construct return string
	ret = ""
	if final_start > -1:
		for j in range(final_start, final_start+final_length):
			ret += s[j]
	return ret

# helper that lowercases chars
def helper_ord(c):
	return ord(c.lower())

print(substring('I have a friend that went to UPenn!','dtah'))
print(substring('aardvarks are bad', 'vard'))