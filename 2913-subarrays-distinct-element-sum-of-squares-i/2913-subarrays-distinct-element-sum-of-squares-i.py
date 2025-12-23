class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        arr=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                temp=nums[i:j+1]
                temp=sorted(temp)
                arr.append(temp)
        c=0
        d={}
        for i in arr:
            s=set(i)
            if len(s) not in d:
                d[len(s)]=1
            else:
                d[len(s)]+=1
        print(d)
        d=sorted(d.items())
        print(d)
        for i in d:
            c=c+i[1]*(i[0]*i[0])
        return c

            
        