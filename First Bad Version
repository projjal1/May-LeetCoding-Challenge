class Solution:
    def firstBadVersion(self, n):
        l=1
        up=n
        middle=0
        while(l<=up):
            middle=(l+up)//2
            if isBadVersion(middle):
                up=middle-1
            else:
                l=middle+1
        return up+1
