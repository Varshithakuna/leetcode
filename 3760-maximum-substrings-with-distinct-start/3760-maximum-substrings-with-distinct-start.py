class Solution(object):
    def maxDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = len(s)
        ans=[]
        for i in s:
            if i not in ans:
                ans.append(i)
        return len(ans)

        