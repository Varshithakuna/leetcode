class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans =[]
        for i in tokens:
            if i=="+":
                k=ans.pop()
                h=ans.pop()
                ans.append(int(k+h))
            elif i=="-":
                k=ans.pop()
                h=ans.pop()
                ans.append(int(h-k))
            elif i=="*":
                k=ans.pop()
                h=ans.pop()
                ans.append(int(k*h))
            elif i=="/":
                k=ans.pop()
                h=ans.pop()
                ans.append(int(h/k))
            else:
                ans.append(int(i))
        return ans[0]
        


        