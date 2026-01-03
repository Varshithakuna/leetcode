class Solution {
    public int[] shuffle(int[] nums, int n) {
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i =0;i<n;i++){
            ans.add(nums[i]);
            ans.add(nums[i+n]);
        }
        System.out.println(ans);
        for(int i =0;i<nums.length;i++){
            nums[i]=ans.get(i);
        }
        return nums;
        
    }
}