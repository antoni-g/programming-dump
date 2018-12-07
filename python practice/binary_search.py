def bin_search(list,tgt):
	first = 0
	last = len(list)-1
	found = False
	while first <= last and not found:
		mid = (first+last)//2
		if list[mid] == tgt:
			found = True
		else:
			if tgt < list[mid]:
				last = mid -1
			else:
				first = mid+1
	return found

#test
l1 = [-4,-3,-2,-1,1,2,3,4,5,6,7,8,9]
print(bin_search(l1,6))
print(bin_search(l1,11))
print(bin_search(l1,-3))