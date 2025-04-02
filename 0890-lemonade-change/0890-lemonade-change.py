class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        f=[]
        c=0
        for i in bills:
            if i==5:
                c=c+1
                f.append(i)
            elif i==10:
                f.append(i)
                if 5 in f:
                    c=c+1
                    f.remove(5)
                else:
                    return False
                    break
            elif i==20:
                f.append(i)
                if 5 in f and 10 in f:
                    c=c+1
                    f.remove(5)
                    f.remove(10)
                elif f.count(5)>=3:
                    c=c+1
                    f.remove(5)
                    f.remove(5)
                    f.remove(5)
                else:
                    return False
                    break
        if c==len(bills):
            return True

            
            
            