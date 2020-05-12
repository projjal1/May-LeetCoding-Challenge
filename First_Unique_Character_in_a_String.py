class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=dict()
        pos=dict()
        it=0
        for each in s:
            if each not in d:
                d[each]=1
                pos[each]=it
            else:
                d[each]+=1
                
            it+=1
        
        m=-1
        for each in d:
            if d[each]!=1:
                continue
            else:
                if m>pos[each] or m==-1:
                    m=pos[each]
                    
        return m
