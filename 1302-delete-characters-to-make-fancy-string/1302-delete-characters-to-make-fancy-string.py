# class Solution:
#     def makeFancyString(self, s: str) -> str:
#         ans=[]
#         for i in range(len(s)):
#             if len(ans)>=2 and ans[-1]==s[i] and ans[-2]==s[i]:
#                 ans.pop()
#                 ans.append(s[i])
#                 print(ans)
#             elif len(ans)>=2 and ans[-1]!=s[i]:
#                 ans.append(s[i])
#                 print(ans)
#             else:
#                 ans.append(s[i])
#         return ''.join(ans)
class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for c in s:
            if len(result) >= 2 and result[-1] == c and result[-2] == c:
                continue
            result.append(c)
        return ''.join(result)

        