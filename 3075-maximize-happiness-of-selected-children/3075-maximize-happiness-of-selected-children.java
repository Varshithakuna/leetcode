class Solution {
    public long maximumHappinessSum(int[] h, int k) {
        int[] c = Arrays.copyOf(h,h.length);
        Arrays.sort(c);
        System.out.println(Arrays.toString(c));
        long ans=0;
        Stack<Integer> arr = new Stack<>();
        for(int i=0;i<c.length;i++){
            arr.push(c[i]);
        }
        if(c.length==0){
            return 0;
        }
        for(int i =0;i<k;i++){
            int m=arr.pop();
            if((m-i)>=0){
                ans=ans+m-i;
            }
        }
        return ans;
        
    }
}