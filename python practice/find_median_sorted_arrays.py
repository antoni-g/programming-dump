class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1[len(nums1)-1] < nums2[0]:
        	pass
        pass

    def bruteForce(self,nums1,nums2):
    	nums1.extend(nums2)
    	return sorted(nums1)

    def find_median(self,nums):
    	if len(nums) % 2 == 0:
    		el1 = nums[len(nums)//2-1]
    		el2 = nums[len(nums)//2]
    		return (el1+el2)/2
    	else:
    		return nums[len(nums)//2+1]

s = Solution()
l1 = [1,2,3,4,5]
l2 = [4,7,9,11]
print(s.find_median(s.bruteForce(l1,l2)))
l1 = [1,2,3,4,5]
l2 = [4,7,8,9,11]
print(s.find_median(s.bruteForce(l1,l2)))