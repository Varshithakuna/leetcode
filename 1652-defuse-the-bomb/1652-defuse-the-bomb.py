class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k==0:
            return [0]*len(code)
        elif k>0:
            ans=[]
            for i in range(len(code)):
                p=0
                for j in range(i+1,k+i+1):
                    p=p+code[j%len(code)]
                ans.append(p)
            return ans
        else:
            ans1=[]
            for i in range(len(code)):
                t=0
                for j in range(i-1,i-1-abs(k),-1):
                    t=t+code[j%len(code)]
                ans1.append(t)
            return ans1


    