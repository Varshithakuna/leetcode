class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans={}
        d={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",
            'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.", 'q':"--.-",'r':".-.",'s':"...",'t':"-",
            'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.." }

        for i in words:
            temp=""
            for j in i:
                temp=temp+d[j]
            if temp not in ans:
                ans[temp]=1
            else:
                ans[temp]=ans[temp]+1
        return len(ans)

    