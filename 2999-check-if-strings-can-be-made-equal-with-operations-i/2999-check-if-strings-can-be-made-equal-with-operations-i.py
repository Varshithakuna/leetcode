class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        k=[]
        for i in s1:
            k.append(i)
        for i in range(len(k)):
            for j in range(len(k)):
                if abs(j-i)==2:
                    k[i],k[j]=k[j],k[i]
                    if("".join(k)==s2):
                        return True
        else:
            return False
        # p=s1[:2]
        # q=s1[2:len(s1)]

        # o=q+p
        # if o==s2:
        #     return True
        # else:
        #     return False

        