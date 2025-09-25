class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        # ans=[]
        # k=""
        # n=""
        # s=0
        # d=0
        # for i in range(len(version1)):
        #     if version1[i]==".":
        #         s=s+i
        # for i in range(len(version2)):
        #     if version2[i]==".":
        #         d=d+i
        # for i in range(s+1,len(version1)):
        #     k=k+version1[i]
        # for i in range(d+1,len(version2)):
        #     n=n+version2[i]
        # ans.append([k,n])
        # if version1.count('.')>1 or version2.count('.')>1:
        #     return 0
        # else:
        #     k=int(k)
        #     n=int(n)
        #     if k>n:
        #         return 1
        #     elif k==n:
        #         return 0
        #     else:
        #         return -1
        v11 = v1.split(".")
        v22 = v2.split(".")
        if len(v11)>len(v22):
            for i in range(len(v11)-len(v22)):
                v22.append(0)
        elif len(v11)<len(v22):
            for j in range(len(v22)-len(v11)):
                v11.append(0)
        ans=[]
        pans=[]
        for i in v11:
            ans.append(int(i))
        for i in v22:
            pans.append(int(i))
        print(ans)
        print(pans)
        c=0
        for i,j in zip(ans,pans):
            if i<j:
                return -1
            elif i>j:
                return 1  
        else:
            return 0

        