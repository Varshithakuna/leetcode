class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        elif num>0:
            num = hex(num)[2:]
            return num
        else:
            num=num+2**32
            num =hex(num)[2:]
            return num
        
        