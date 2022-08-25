class Solution {
    public int maxProduct(int[] nums) {
        int a = nums[0], b = nums[0], ans = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int n = nums[i];
            int prevMax = a;
            a = Math.max(a * n, Math.max(n, b * n));
            b = Math.min(prevMax * n, Math.min(b * n, n));
            System.out.println(a + " " + b);
            ans = Math.max(a, ans);
        }
        return ans;
    }
}