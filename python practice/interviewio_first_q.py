# given a list of floats ->
# insert an operator between each two numbers to find the maximum possible 
# read left to right with equal weight (no order of operations)
# value for the entire list
# ie -> [1,12,-3]
# solution: [1 - 12 * 3]

import sys
class Solution(object):

	def max_val(self,nums):
		if len(nums) == 0:
			return None
		self.max = -1* (sys.maxsize/2)
		self.recurse(1,nums,nums[0])
		return self.max;

	def recurse(self,index,nums,curr):
		if index == len(nums):
			if curr > self.max:
				self.max = curr
		else:
			self.recurse(index+1,nums,curr+nums[index])
			self.recurse(index+1,nums,curr-nums[index])
			self.recurse(index+1,nums,curr*nums[index])
			self.recurse(index+1,nums,curr/nums[index])

s = Solution()
# should be 132
test = [1,12,-3,4]
print('Testing:')
print(s.max_val(test))