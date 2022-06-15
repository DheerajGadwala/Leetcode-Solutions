class Solution {
    
    String all = "qwertyuiopasdfghjklzxcvbnm";
    Set<String> words;
    Map<String, Integer> mem;
    
    public int longestStrChain(String[] words) {
        this.words = new HashSet<>();
        mem = new HashMap<>();
        
        for (String word: words) {
            this.words.add(word);
        }
        
        int ans= 0;
        
        for (String word: words) {
            ans = Math.max(ans, res(word));
        }
        
        return ans;
        
    }
    
    int res(String curr) {
        if (mem.containsKey(curr)) {
            return mem.get(curr);
        }
        int ret = 0;
        for (char c: all.toCharArray()) {
            for (int i = 0; i <= curr.length(); i++) {
                String next = curr.substring(0, i) + c + curr.substring(i);
                if (words.contains(next)) {
                    ret = Math.max(ret, res(next));
                }
            }
        }
        mem.put(curr, 1+ret);
        return 1 + ret;
    }
}