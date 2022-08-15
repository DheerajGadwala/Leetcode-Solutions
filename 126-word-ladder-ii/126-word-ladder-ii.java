class Solution {
    
    Set<String> wordSet;
    String endWord;
    Map<String, List<List<String>>> cache;
    
    boolean canBeNext(String cur, String next) {
        int diffCount = 0;
        for (int i = 0; i< cur.length(); i++) {
            if (cur.charAt(i) != next.charAt(i))
                diffCount++;
        }
        return diffCount == 1;
    }
    
    
    List<List<String>> dfs(String u, int dep) {
        if (cache.containsKey(u+dep)) {
            return cache.get(u+dep);
        }
        else if (dep == 1 && u.equals(endWord)) {
            List<List<String>> ret = new ArrayList<>();
            List<String> path = new ArrayList<>();
            path.add(u);
            ret.add(path);
            return ret;
        }
        else if (dep == 1) {
            return new ArrayList<>();
        }
        else {
            List<List<String>> all = new ArrayList<>();
            for (String v: wordSet) {
                if (canBeNext(u, v)) {
                    all.addAll(dfs(v, dep - 1));
                }
            }
            List<List<String>> ret = new ArrayList<>();
            for (List<String> l: all) {
                List<String> temp = new ArrayList<>(l);
                temp.add(0, u);
                ret.add(temp);
            }
            cache.put(u+dep, ret);
            return ret;
        }
    }
    
    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        wordSet = new HashSet<>(wordList);
        this.endWord = endWord;
        cache = new HashMap<>();
        Queue<String> q = new LinkedList<>();
        Map<String, Integer> dist = new HashMap<>();
        q.add(beginWord);
        dist.put(beginWord, 1);
        
        while (q.size() != 0) {
            String u = q.poll();
            if (u.equals(endWord)) {
                break;
            }
            for (String v: wordList) {
                if (canBeNext(u, v) && !dist.containsKey(v)) {
                    dist.put(v, dist.get(u) + 1);
                    q.add(v);
                }
            }
        }
        
        int d = dist.getOrDefault(endWord, 0);
        if (d == 0) {
            return new ArrayList<>();
        }
        return dfs(beginWord, d);
        
        
    }
}