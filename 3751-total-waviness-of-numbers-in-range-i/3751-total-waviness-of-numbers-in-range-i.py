class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        c=0
        if len(str(num1))<=2 and len(str(num2))<=2:
            return 0
        else:
            for o in range(num1,num2+1):
                i = str(o)
                k=0
                for j in range(1,len(i)-1):
                    if int(i[j-1])>int(i[j]) and int(i[j])<int(i[j+1]):
                        k=k+1
                    elif int(i[j-1])<int(i[j]) and int(i[j])>int(i[j+1]):
                        k=k+1
                c=c+k
        return c



        