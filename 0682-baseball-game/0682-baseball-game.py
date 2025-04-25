from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for op in operations:
            if op == "C":
                if ans:
                    ans.pop()
            elif op == "D":
                if ans:
                    ans.append(2 * ans[-1])
            elif op == "+":
                if len(ans) >= 2:
                    ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(op))
        return sum(ans)

        