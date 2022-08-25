class Solution {
    
    int[] nums;
    Boolean[][] cache;
    static boolean truth = false;
    
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int i: nums) {
            sum += i;
        }
        if (sum % 2 == 1) return false;
        sum = sum / 2;    
        this.nums = nums;
        cache = new Boolean[nums.length + 1][sum+1];
        truth = false;
        return par(0, sum);
    }
    
    private boolean par (int pos, int tar) {
        if (pos == nums.length || tar < 0) {
            return false;
        }
        else if (tar == 0) {
            truth = true;
            return true;
        }
        if (cache[pos][tar] != null) {
            return cache[pos][tar];
        }
        else {
            cache[pos][tar] = truth || par(pos + 1, tar - nums[pos]) || par(pos + 1, tar);
            return cache[pos][tar];
        }
    }
    
    
    
}