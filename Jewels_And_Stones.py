class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        cnt=0
        for each in J:
            cnt+=S.count(each)
            
        return cnt
