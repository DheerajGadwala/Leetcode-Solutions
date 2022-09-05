class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        
        Deque<Integer> q = new LinkedList<>();
        int n = chargeTimes.length, f = 0, l = 0, ans = 0;
        long currSum = 0;
        
        while (f < n) {
            while (q.size() > 0 && chargeTimes[q.peekLast()] < chargeTimes[f]) q.pollLast();
            q.addLast(f);
            currSum += runningCosts[f++];
            while (f!=l && chargeTimes[q.peekFirst()]+(f-l)*currSum > budget) {
                if (q.peekFirst() == l) q.pollFirst();
                currSum -= runningCosts[l++];
            }
            ans = Math.max(ans, f-l);
        }
        
        return ans;
    }
}