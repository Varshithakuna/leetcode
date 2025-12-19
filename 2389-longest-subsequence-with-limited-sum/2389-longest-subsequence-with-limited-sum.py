class Solution:
    def answerQueries(self, nums: List[int], q: List[int]) -> List[int]:
        nums=sorted(nums)
        k=[]
        for i in q:
            b=0
            c=[]
            for j in nums:
                b=b+j
                if b<=i:
                    b=b+j
                    c.append(j)
                b=b-j
            print(c)
            k.append(len(c))

        print(k)
        return k
                    
                




        