class Solution(object):
    def removeElement(self, nums, val):
#         let say k is at index 0 at first
        k = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k
        
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        