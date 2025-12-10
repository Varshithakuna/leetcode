class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # ans=[]
        # for i in range(len(arr)-1):
        #     maxi=0
        #     for j in range(i+1,len(arr)):
        #         n=max(arr[j],maxi)
        #         maxi=n
        #     ans.append(maxi)
        # ans.append(-1)
        # return ans
        maxi=arr[-1]
        arr[-1]=-1
        for i in range(len(arr)-2,-1,-1):
            ele = arr[i]
            arr[i]=maxi
            if ele>maxi:
                maxi = ele 
        return arr



        