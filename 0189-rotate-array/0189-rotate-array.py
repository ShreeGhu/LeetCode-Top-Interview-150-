class Solution(object):
    def rotate(self, nums, k):
        
        k = k % len(nums)
        start = 0
        end = len(nums)-1
        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start +=1
            end -=1
            
        start = 0
        end = k-1
        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start +=1
            end -=1
            
        start = k
        end = len(nums)-1
        while start < end:
            nums[start],nums[end] = nums[end], nums[start]
            start +=1
            end -=1

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        