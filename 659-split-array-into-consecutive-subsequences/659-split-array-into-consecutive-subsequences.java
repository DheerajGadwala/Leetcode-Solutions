class Solution {
    public boolean isPossible(int[] nums) {
        
        PriorityQueue<Integer[]> q = new PriorityQueue<>((o1, o2) -> {
            if (o1[0] == o2[0]) {
                return Integer.compare(o1[1], o2[1]);
            }
            else {
                return Integer.compare(o1[0], o2[0]);
            }
        });
        
        for (int i: nums) {
            while (q.size() != 0 && q.peek()[0] < i - 1) {
                Integer[] u = q.poll();
                if (u[1] < 3) {
                    return false;
                }
            }
            if (q.size() == 0) {
                q.add(new Integer[] {i, 1});
            }
            else if (q.peek()[0] < i) {
                Integer[] u = q.poll();
                u[0] = i;
                u[1] += 1;
                q.add(u);
            }
            else {
                q.add(new Integer[] {i, 1});
            }
        }
        while (q.size() != 0) {
            if (q.poll()[1] < 3) {
                return false;
            }
        }
        return true;
    }
}