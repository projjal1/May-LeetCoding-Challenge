class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_elem=0
        max_count=0
        d=dict()
        
        for each in nums:
            if each not in d:
                d[each]=1
                if max_count<1:
                    max_count=1
                    max_elem=each
                    
            else:
                d[each]+=1
                if d[each]>max_count:
                    max_count=d[each]
                    max_elem=each
                    
        return (max_elem)
