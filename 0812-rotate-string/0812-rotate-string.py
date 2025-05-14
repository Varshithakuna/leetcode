class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ans=[]
        for i in range(len(s)):
            l=s[:i+1:]
            r=s[i+1::]
            m=(r+l)
            if m==goal:
                return True
        else:
            return False
    
        

                
        
            
        