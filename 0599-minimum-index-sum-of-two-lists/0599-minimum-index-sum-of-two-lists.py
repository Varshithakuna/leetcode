class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans=0
        p=[]
        m=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                k= list2.index(list1[i])
                ans=i+k
                p.append([list1[i],i+k])
                m.append(i+k)
        q=[]
        h=(min(m))
        for i in p:
            if i[1]==h:
                q.append(i[0])



        return q




        