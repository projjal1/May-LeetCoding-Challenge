class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trusted=dict()
        trusts=dict()
        for each in range(1,N+1):
            trusted[each]=0
            trusts[each]=0
        for x,y in trust:
            trusted[y]+=1
            trusts[x]+=1
        for each in trusted:
            if trusted[each]==N-1 and trusts[each]==0:
                return each
        return -1
