class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String, Integer> cnt = new HashMap<>();
        for (String word: words) {
            cnt.put(word, cnt.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<String> q = new PriorityQueue<>((a,b) -> {
            int cmp = Integer.compare(cnt.get(b), cnt.get(a));
            if (cmp != 0) {
                return cmp;
            }
            else {
                return a.compareTo(b);
            }
        });
        for (String word: cnt.keySet()) {
            q.add(word);
        }
        List<String> ret = new ArrayList<>();
        while (k > 0 && q.size() > 0) {
            ret.add(q.poll());
            k--;
        }
        return ret;
    }
}