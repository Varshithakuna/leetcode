class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if len(nums[i:j])==k:
                    ans.append(nums[i:j])
        a=[]
        for i in nums:
            c=0
            for j in ans:
                if i in j:
                    c=c+1
            if c==1:
                a.append([c,i])
        print(a)
        # if a:
        #     k1=min(a)
        #     s=0
        #     for i in range(len(a)):
        #         if a[i]==k1 :
        #             s=max(s,nums[i])
        #     print(s)
        #     return s
        a=sorted(a, key=lambda x: x[0])
        print(a)
        if a:
            n=0
            m=a[0][0]
            for i in a:
                if i[0]==m:
                    n=max(n,i[1])
            return n
        return -1
            

            



        