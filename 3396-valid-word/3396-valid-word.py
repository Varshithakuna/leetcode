class Solution:
    def isValid(self, word: str) -> bool:
        word=word.lower()
        word=list(str(word))
        if len(word)>=3:
            a=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]
            b=["0","1","2","3","4","5","6","7","8","9"]
            c=["a","e","i","o","u"]
            d=0
            s=0
            p=0
            k=0
            for i in word:
                if i in a:
                    p=p+1
                elif i in b:
                    d=d+1
                elif i in c:
                    s=s+1
                else:
                    k=k+1

                
            if p>0  and s>0 and k==0:
                return True
            else:
                return False
        else:
            return False
        

        