class Solution(object):
    def hIndex(self, citations):
        
        citations.sort()
        n = len(citations)
        
        for index, value in enumerate(citations):
            if n - index <= value:
                return n - index
        return 0
        
        
        
        """
        :type citations: List[int]
        :rtype: int
        """
        