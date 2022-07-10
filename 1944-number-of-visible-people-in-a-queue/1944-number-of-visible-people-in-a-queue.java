class Solution {
    public int[] canSeePersonsCount(int[] heights) {
        Stack<Integer> s = new Stack<>();
        int[] ans = new int[heights.length];
        for (int i = heights.length - 1; i >= 0; i--) {
            int cnt = 0;
            while (!s.empty() && s.peek() < heights[i]) {
                s.pop();
                cnt++;
            }
            s.push(heights[i]);
            ans[i] = cnt + (s.size() == 1 ? 0 : 1);
        }
        return ans;
    }
}