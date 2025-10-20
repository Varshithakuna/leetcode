class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        count = 0
        for i in operations:
            if (i =="--X" ):
                count = count-1
            elif (i=="X--"):
                count=count-1
            else:
                count=count+1
        return count
        