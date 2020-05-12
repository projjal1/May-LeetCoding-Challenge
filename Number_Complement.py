class Solution:
    def findComplement(self, num: int) -> int:
        s=bin(num)
        s=s[2:]
        new=''
        for each in range(len(s)):
            if s[each]=='1':
                new=new+'0'
            else:
                new=new+'1'
        
        l=len(new)-1
        no=0
        itr=0
        while(l>=0):
            no+=int(new[itr])*(2**l)
            itr+=1
            l-=1
        return no
