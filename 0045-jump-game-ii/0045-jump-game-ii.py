class Solution(object):
    def jump(self, nums):
        
        
        jumps = 0
        l=r =0
        
        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1): #inclusive to add the element at right
                    farthest = max(farthest, i + nums[i])
            l = r + 1
            jumps +=1
            r = farthest
        return jumps
        """
        :type nums: List[int]
        :rtype: int
        """
        