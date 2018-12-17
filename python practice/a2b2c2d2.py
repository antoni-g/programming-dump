# given n, finds all int pairs from 1 to n that
# satisfy a^2 + b^2 = c^2 + d^2
def solve(n):
	pairs = {}
	for i in range(1,n+1):
		for j in range(1,n+1):
			res = i**2+j**2
			if res in pairs:
				pairs[res].append((i,j))
			else:
				pairs[res] = [(i,j)]
	for el in pairs.keys():
		for first in pairs[el]:
			for second in pairs[el]:
				print(str(first)+', '+str(second))

solve(100)
