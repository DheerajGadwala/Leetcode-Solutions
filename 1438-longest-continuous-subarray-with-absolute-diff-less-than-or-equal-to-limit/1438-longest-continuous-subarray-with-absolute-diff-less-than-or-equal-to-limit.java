class Solution {
    public int longestSubarray(int[] nums, int limit) {
        
        // min Queue [increaasing], max Queue [decreasing]
        Deque<Integer> minQ = new LinkedList<>(), maxQ = new LinkedList<>();
        // first, last
        int f = 0, l = 0, ans = 0;
        
        while (f < nums.length) {
            // maintaining the monotonic property
            while (minQ.size() > 0 && nums[minQ.peekLast()] > nums[f]) minQ.pollLast();
            while (maxQ.size() > 0 && nums[maxQ.peekLast()] < nums[f]) maxQ.pollLast();
            minQ.add(f);
            maxQ.add(f);
            f++;
            // correcting the l pointer for the current f pointer
            while (nums[maxQ.peekFirst()] - nums[minQ.peekFirst()] > limit) {
                if (maxQ.peekFirst() == l) {
                    maxQ.pollFirst();
                }
                if (minQ.peekFirst() == l) {
                    minQ.pollFirst();
                }
                l++;
            }
            ans = Math.max(ans, f-l);
        }
        return ans;
    }
}