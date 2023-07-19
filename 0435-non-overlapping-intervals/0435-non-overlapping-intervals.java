class Solution {

	// We find the set of intervals with the maximum size that is non-overlapping.
	// Our answer will be the (total intervals - the maximum size that we find) 
	
    public int eraseOverlapIntervals(int[][] intervals) {
        
		// Sort by finish time followed by start time
        Arrays.sort(intervals, (int[] o1, int[] o2) -> {
            int x = Integer.compare(o1[1], o2[1]);
            int y = Integer.compare(o1[0], o1[0]);
            return x != 0 ? x : y;
        });
        
		// start time can not be lower than this.
        int time = -50001, ans = 0;
        
        // Works because greedy always stays ahead.
		for (int[] interval: intervals) {
        
            if (interval[0] >= time) {
                time = interval[1];
                ans++;
            }
        }
        
        return intervals.length - ans;
    }
}