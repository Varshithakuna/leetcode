class Solution:
    def makeFancyString(self, s: str) -> str:
        ans=[]
        for i in s:
            if len(ans)>=2 and ans[-1]==i and ans[-2]==i:
                continue
                print(ans)
            else:
                ans.append(i)
        return ''.join(ans)
# class Solution:
#     def makeFancyString(self, s: str) -> str:
#         result = []
#         for c in s:
#             if len(result) >= 2 and result[-1] == c and result[-2] == c:
#                 continue
#                 print(result)
#             result.append(c)
#         return ''.join(result)

        