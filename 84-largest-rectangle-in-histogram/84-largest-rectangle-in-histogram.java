class Solution {
    
    public int largestRectangleArea(int[] heights) {
        
        Stack<Integer[]> s = new Stack<>();
        int ans = 0;
        
        for (int i = 0; i < heights.length; i++) {
            int l = i;
            while (!s.empty() && heights[s.peek()[0]] >= heights[i]) {
                l = s.peek()[1];
                ans = Math.max(ans, (i - s.peek()[1]) * heights[s.peek()[0]]);
                s.pop();
            }
            s.push(new Integer[] {i, l});
        }
        int r = s.peek()[0];
        while (!s.empty()) {
            ans = Math.max(ans, (r - s.peek()[1] + 1) * heights[s.peek()[0]]);
            s.pop();
        }
        return ans;
        
    }
}