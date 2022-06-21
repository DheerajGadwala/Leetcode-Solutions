class Solution {

    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> q = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return -Integer.compare(a, b);
            }
        });
        for (int i = 1; i < heights.length; i++) {
            if (heights[i] > heights[i-1]) {
                int diff = heights[i] - heights[i-1];
                if (bricks >= diff) {
                    bricks -= diff;
                    q.add(diff);
                }
                else if (ladders > 0) {
                    if (q.size() > 0 && diff < q.peek()) {
                        bricks += q.poll()-diff;
                        ladders--;
                        q.add(diff);
                    }
                    else {
                        ladders--;
                    }
                }
                else {
                    return i-1;
                }
            }
        }
        return heights.length-1;
    }
}