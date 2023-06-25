class Solution {
    public int nextGreaterElement(int n) {
        char[] nums_ch = String.valueOf(n).toCharArray();
        int l = nums_ch.length;
        int[] nums = new int[l];
        for (int i = 0; i < l; i++) {
            nums[i] = nums_ch[i] - '0';
        }
        Integer first = null, last = null;
        for (int i = 1; i < l; i++) {
            if (nums[i-1] < nums[i]) {
                    first = i-1;
                    last = i;
            }
            if (first != null && nums[last] >= nums[i] && nums[i] > nums[first])
                last = i;
        }
        if (first == null) return -1;
        
        nums[first] += nums[last];
        nums[last] = nums[first] - nums[last];
        nums[first++] -= nums[last];
        
        int x = l - 1;
        while (first < x) {
            nums[first] += nums[x];
            nums[x] = nums[first] - nums[x];
            nums[first++] -= nums[x--];
        }
        
        int ret = 0;
        for (int i = 0; i < l; i++) {
            if (ret * 10 + nums[i] < ret) return -1;
            ret *= 10;
            ret += nums[i];
        }
        return ret;
    }
}