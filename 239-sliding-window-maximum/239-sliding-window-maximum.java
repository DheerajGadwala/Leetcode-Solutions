class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        
        Deque<Integer> q = new LinkedList<>();
        int n = nums.length;
        int[] ret = new int[n-k+1];
        
        for (int i = 0; i < n; i++) {
            while (q.size() > 0 && nums[q.peekFirst()] < nums[i]) q.pollFirst();
            q.addFirst(i);
            if (i >= k-1) {
                if (i-k == q.peekLast()) q.pollLast();
                ret[i-k+1] = nums[q.peekLast()];
            }
        }
        
        return ret;
    }
}