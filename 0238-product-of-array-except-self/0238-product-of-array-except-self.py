class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        # ans =[]
        # for i in range(len(nums)):
        #     p=[]
        #     s=nums[i]
        #     for i in nums:
        #         if i!=s:
        #             p.append(i)
        #     j=1
        #     for i in p:
        #         if i!=0:
        #             j=j*i
        #         ans.append(j)
        #     else:
        #         ans.append(0)

        # return ans
        prefix=[1]
        sufix=[1]
# findng prefix---------------------
        mul=1
        for i in range(len(arr)-1):
            mul*=arr[i]
            prefix.append(mul)

# findng sufix---------------------
        mul=1
        for i in range(len(arr)-1,0,-1):
            mul*=arr[i]
            sufix.insert(0,mul)

# findng answer---------------------
        answer=[]
        for i in range(len(arr)):
            answer.append(sufix[i]*prefix[i])

        return answer
        
            
            


        