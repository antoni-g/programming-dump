# must be a sorted array
def two_sum(ints,tgt):
	front = 0
	end = len(ints)-1
	if end < 1:
		return None
	while (front != end):
		sum = ints[front]+ints[end]
		if (sum == tgt):
			return (ints[front], ints[end])
		else:
			if sum < tgt:
				front += 1
			else:
				end -= 1
	return None

l1 = [2,4,5,7,8,9]
print(two_sum(l1,13))

l2 = [-51,2,3,4,5,6,7,8,9,111,3342,4332421]
print(two_sum(l2,116))