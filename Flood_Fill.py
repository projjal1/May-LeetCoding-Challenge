class Solution:
    def check(self,d,row,col,lr,lc):
        if (row<lr and row>=0) and (col<lc and col>=0):
            if d[row,col]==0:
                return True
            else:
                return False 
        return False
    
    def color(self,d,image,row,col,lr,lc,newColor,pc):
        d[row,col]=1
        
        nc=image[row][col]
        if nc!=pc:
            return
        
        #Upper
        if self.check(d,row-1,col,lr,lc):
            self.color(d,image,row-1,col,lr,lc,newColor,nc)
        #Right
        if self.check(d,row,col+1,lr,lc):
            self.color(d,image,row,col+1,lr,lc,newColor,nc)
        #Left 
        if self.check(d,row,col-1,lr,lc):
            self.color(d,image,row,col-1,lr,lc,newColor,nc)
        #Down
        if self.check(d,row+1,col,lr,lc):
            self.color(d,image,row+1,col,lr,lc,newColor,nc)
    
        #Set color of that pixel to new color
        image[row][col]=newColor
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        lr=len(image)
        lc=len(image[0])
        
        #Dictionary of traversed indices
        d=dict()

        #Set all to zero
        for x in range(lr):
            for y in range(lc):
                d[x,y]=0
                
        self.color(d,image,sr,sc,lr,lc,newColor,image[sr][sc])
        
        return image
