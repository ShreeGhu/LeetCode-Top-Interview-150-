class Solution(object):
    def removeDuplicates(self, nums):
        k = 0 #lets give index of '0' for K
        
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[k] = nums[i]
                k +=1
        
        nums[k] = nums[len(nums)-1]
        k +=1
        return k
    
    
                
        """
        :type nums: List[int]
        :rtype: int
        """
        