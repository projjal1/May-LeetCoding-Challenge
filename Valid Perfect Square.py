class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==0 or num==1:
            return True
        for i in range(1,num):
            get_sqr=i*i
            if get_sqr>num:
                return False
            elif get_sqr==num:
                return True
            else:
                continue
