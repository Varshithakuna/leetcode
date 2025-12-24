class Solution {
    public int minimumBoxes(int[] apple, int[] c) {

        int n[] = Arrays.copyOf(c,c.length);
        Arrays.sort(n);
        int m[] = new int[c.length];
        for(int i=c.length-1;i>=0;i--){
            m[i]=n[(c.length-1)-i];
        }
        int k =0;
        int h =0;
        for(int i =0;i<=m.length-1;i++){
            if(k<Arrays.stream(apple).sum()){
                k=k+m[i];
                h=h+1;
            }
        }
        return h;

        
    }
}