class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> cnt = new HashMap<>();
        for (String word: words) {
            cnt.put(word, cnt.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<String> q = new PriorityQueue<>((a,b) -> {
            int cmp = Integer.compare(cnt.get(b), cnt.get(a));
            if (cmp != 0) {
                return -cmp;
            }
            else {
                return -a.compareTo(b);
            }
        });
        for (String word: cnt.keySet()) {
            if (q.size() < k) {
                q.add(word);
            }
            else {
                q.add(word);
                q.poll();
            }
        }
        List<String> ret = new ArrayList<>();
        
        while (q.size() > 0) {
            ret.add(q.poll());
        }
        int i = 0, j = k - 1;
        while (i < j) {
            String temp = ret.get(i);
            ret.set(i, ret.get(j));
            ret.set(j, temp);
            i++;j--;
        }
        return ret;
    }
}