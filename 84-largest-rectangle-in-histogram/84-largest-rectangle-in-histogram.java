class Solution {
    
    public int largestRectangleArea(int[] heights) {
        
        Stack<Integer[]> s = new Stack<>();
        int[] answers = new int[heights.length];
        
        for (int i = heights.length-1; i >= 0; i--) {
            int h = i;
            while (!s.empty() && s.peek()[0] >= heights[i]) {
                h =s.pop()[1];
            }
            s.add(new Integer[] {heights[i], h});
            answers[i] = heights[i] * (h - i + 1);
        }
        
        s = new Stack<>();
        
        for (int i = 0; i < heights.length; i++) {
            int h = i;
            while (!s.empty() && s.peek()[0] >= heights[i]) {
                h =s.pop()[1];
            }
            s.add(new Integer[] {heights[i], h});
            answers[i] += heights[i] * (i - h);
        }
        
        int ret = 0;
        for (int k: answers) {
            ret = Math.max(ret, k);
        }
        
        return ret;
        
    }
}