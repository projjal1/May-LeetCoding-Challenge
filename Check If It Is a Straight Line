class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        l=len(coordinates)

        #initial value of slope
        y1=coordinates[1][1]
        y0=coordinates[0][1]
        x1=coordinates[1][0]
        x0=coordinates[0][0]

        ydiff=y1-y0
        xdiff=x1-x0

        if xdiff==0:
            m=9999
        else:
            m=ydiff/xdiff
    
        for i in range(1,l-1):
        
            y1=coordinates[i+1][1]
            y0=coordinates[i][1]
            x1=coordinates[i+1][0]
            x0=coordinates[i][0]

            ydiff=y1-y0
            xdiff=x1-x0

            m_inter=0
            
            if xdiff==0:
                m_inter=999
            else:
                m_inter=ydiff/xdiff
        
            if m_inter!=m:
                return False
            
        return True
