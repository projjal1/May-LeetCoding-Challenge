class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d1=dict()
        d2=dict()
        
        for each in ransomNote:
            if each not in d1:
                d1[each]=1
            else:
                d1[each]+=1
                
        for each in magazine:
            if each not in d2:
                d2[each]=1
            else:
                d2[each]+=1
                
        for x in d1:
            val1=d1[x]
            try:
                val2=d2[x]
                if val2<val1:
                    return False
            except:
                return False
        return True
