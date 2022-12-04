class Solution {
    
    public String frequencySort(String s) {
        if(s == null || s.length() == 0) return "";
        
        Map<Character, Integer> freq = new HashMap<>();
        for (char c: s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        
        PriorityQueue<Character> q = new PriorityQueue<>((a, b) -> {
           int ret = Integer.compare(freq.get(b), freq.get(a));
            if (ret == 0) ret = Character.compare(a, b);
            return ret;
        });
        
        for (char c: s.toCharArray()) {
            q.add(c);
        }
        
        StringBuilder ret = new StringBuilder();
        while (q.size() != 0) ret.append(q.poll());
        return ret.toString();
        
    }
}