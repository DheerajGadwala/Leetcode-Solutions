class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> q = new PriorityQueue<>((a, b) -> Integer.compare(b, a));
        for (int s: stones) {
            q.add(s);
        }
        while (q.size() > 1) {
            q.add(q.poll() - q.poll());
        }
        return q.size() == 0 ? 0 : q.poll();
    }
}