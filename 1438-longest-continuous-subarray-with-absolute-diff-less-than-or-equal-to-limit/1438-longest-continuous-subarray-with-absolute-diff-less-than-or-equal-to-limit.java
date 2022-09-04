class Solution {
    public int longestSubarray(int[] nums, int limit) {
        
        // min Stack and x Stack
        Deque<Integer> minQ = new LinkedList<>(), maxQ = new LinkedList<>();
        int f = 0, l = 0, ans = 0;
        
        while (f < nums.length) {
            while (minQ.size() > 0 && nums[minQ.peekLast()] > nums[f]) minQ.pollLast();
            while (maxQ.size() > 0 && nums[maxQ.peekLast()] < nums[f]) maxQ.pollLast();
            minQ.add(f);
            maxQ.add(f);
            f++;
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