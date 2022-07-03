class Solution {
    public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
        Arrays.sort(horizontalCuts);
        Arrays.sort(verticalCuts);
        
        long a = Math.max(horizontalCuts[0], h - horizontalCuts[horizontalCuts.length - 1]);
        long b = Math.max(verticalCuts[0], w - verticalCuts[verticalCuts.length - 1]);
        
        for (int i = 1; i < horizontalCuts.length; i++) {
            a = Math.max(a, horizontalCuts[i] - horizontalCuts[i - 1]);
        }
        
        for (int i = 1; i < verticalCuts.length; i++) {
            b = Math.max(b, verticalCuts[i] - verticalCuts[i - 1]);
        }
        
        return (int) ((a * b) % 1000000007);
    }
}