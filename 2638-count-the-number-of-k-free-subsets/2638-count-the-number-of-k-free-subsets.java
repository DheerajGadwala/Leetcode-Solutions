class Solution {
    public long countTheNumOfKFreeSubsets(int[] nums, int k) {
        Arrays.sort(nums);
        List<Integer>[] lists = new ArrayList[k];
        long ans = 1;
        for (int i = 0; i < k; i++) {
            lists[i] = new ArrayList<>();
        }
        for (int n: nums) {
            lists[n % k].add(n);
        }
        for (int i = 0; i < k; i++) {
            long a = 1, b = 2;
            List<Integer> list = lists[i];
            int m = list.size();
            if (m == 0) continue;
            for(int j = m - 2; j > -1; j--) {
                if (list.get(j) + k == list.get(j + 1)) {
                    long c = a + b;
                    a = b;
                    b = c;
                }
                else {
                    a = b;
                    b *= 2;
                }
            }
            ans *= b;
        }
        return ans;
    }
    
}