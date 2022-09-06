class Solution {
    
    class Pair implements Comparable<Pair> {
        int num, diff;
        
        public Pair(int num, int diff){
            this.num = num;
            this.diff = diff;
        }
        
        @Override
        public int compareTo(Pair pair){
            int res = Integer.compare(diff, pair.diff);
            if (res == 0) return Integer.compare(num, pair.num);
            else return res;
        }
    }
    
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        PriorityQueue<Pair> q = new PriorityQueue<>();
        for (int i = 0; i < arr.length; i++) {
            q.add(new Pair(arr[i], Math.abs(arr[i] - x)));
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < k; i++) {
            res.add(q.poll().num);
        }
        Collections.sort(res);
        return res;
    }
}