class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        ans=[]
        r=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        for value in d.values():
            if len(value)>1:
                ans.append(value)
        for i in ans:
            print(i)
            if abs((min(i))-(max(i)))<=k:
                return True
            if len(i)>2:
                r.append(i)
        print(r)
        for i in r:
            for j in range(len(i)-1):
                if abs(i[j]-i[j+1])<=k:
                    return True
        else:
            return False

            





        