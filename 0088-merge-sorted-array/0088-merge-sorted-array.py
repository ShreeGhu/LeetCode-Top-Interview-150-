class Solution(object):
    def merge(self, nums1, m, nums2, n):

        #last element at nums1
        last_element = m + n -1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last_element] = nums1[m-1]
                m -=1
            else:
                nums1[last_element] = nums2[n-1]
                n -=1
            last_element -=1
        

        #filling the remaining elements from nums2
        while n > 0:
            nums1[last_element] = nums2[n-1]
            n -=1
            last_element -=1

