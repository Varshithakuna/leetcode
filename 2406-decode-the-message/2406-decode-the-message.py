class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        n=[]
        message=list(message)
        ans=""
        for i in key:
            if i not in n and i!=" ":
                n.append(i)
        m="abcdefghijklmnopqrstuvwxyz"
        m=list(m)
        a=[]
        for i in message:
            if i!=" ":
                h = n.index(i)
                a.append(m[h])
            else:
                a.append(" ")
        return "".join(a)


               
