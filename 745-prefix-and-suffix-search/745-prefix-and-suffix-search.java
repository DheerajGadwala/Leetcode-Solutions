class WordFilter {
    
    static class TrieNode {
        
        Map<Character, TrieNode> children;
        boolean endPoint = false;
        
        TrieNode() {
            children = new HashMap<>();
        }
        
        void add(char c) {
            children.put(c, new TrieNode());
        }
        
        boolean contains(char c) {
            return children.containsKey(c);
        }
        
        TrieNode get(char c) {
            return children.get(c);
        }
    }
    
    static class BiTrie {
        
        TrieNode forward, backward;
        Map<String, Integer> ind;
        
        BiTrie() {
            forward = new TrieNode();
            backward = new TrieNode();
            ind = new HashMap<>();
        }
        
        void add(String word, int index) {
            
            TrieNode curr = forward;
            
            for (char c: word.toCharArray()) {
                
                if (curr.contains(c)) {
                    curr = curr.get(c);
                }
                else {
                    curr.add(c);
                    curr = curr.get(c);
                }
            }
            
            curr.endPoint = true;
            
            curr = backward;
            
            for (int i = word.length() - 1; i > -1; i--) {
                char c = word.charAt(i);
                
                if (curr.contains(c)) {
                    curr = curr.get(c);
                }
                else {
                    curr.add(c);
                    curr = curr.get(c);
                }
            }
            
            curr.endPoint = true;
            
            ind.put(word, index);
        }
        
        Set<String> getForwardSuggestions(String word) {
            
            TrieNode curr = forward;
            String src = "";
            
            for (int i = 0; i < word.length(); i++) {
                
                char c = word.charAt(i);
                src += c;
                curr = curr.get(c);
            
                if (curr == null) {
                    return new HashSet<>();
                }
                
            }
            
            Set<String> ret = new HashSet<>();
            Map<TrieNode, String> words = new HashMap<>();
            Queue<TrieNode> q = new LinkedList<>();
            q.add(curr);
            words.put(curr, src);
            
            while (q.size() != 0) {
                
                TrieNode u = q.poll();
                if (u.endPoint) {
                    ret.add(words.get(u));
                }
                
                for (char k: u.children.keySet()) {
                    TrieNode v = u.get(k);
                    q.add(v);
                    words.put(v, words.get(u) + k);
                }
                
            }
            
            return ret;
            
        }
        
        Set<String> getBackwardSuggestions(String word) {
            
            TrieNode curr = backward;
            String src = "";
            
            for (int i = word.length() - 1; i > -1; i--) {
                
                char c = word.charAt(i);
                src = c + src;
                curr = curr.get(c);
                
                if (curr == null) {
                    return new HashSet<>();
                }
            }
            
            HashSet<String> ret = new HashSet<>();
            Map<TrieNode, String> words = new HashMap<>();
            Queue<TrieNode> q = new LinkedList<>();
            q.add(curr);
            words.put(curr, src);
            
            while (q.size() != 0) {
                
                TrieNode u = q.poll();
                if (u.endPoint) {
                    ret.add(words.get(u));
                }
                
                for (char k: u.children.keySet()) {
                    TrieNode v = u.get(k);
                    q.add(v);
                    words.put(v, k + words.get(u));
                }
                
            }
            
            return ret;
            
        }
        
        int search(String pre, String suff) {
            
            Set<String> suggestions = getForwardSuggestions(pre);
            suggestions.retainAll(getBackwardSuggestions(suff));
            
            int ans = -1;
            
            for (String word: suggestions) {
                ans = Math.max(ans, ind.get(word));
            }
            
            return ans;
            
        }
        
        
    }
    
    BiTrie b;
    
    public WordFilter(String[] words) {
        b = new BiTrie();
        for (int i = 0; i < words.length; i++) {
            b.add(words[i], i);
        }
    }
    
    public int f(String prefix, String suffix) {
        return b.search(prefix, suffix);
    }
}

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(prefix,suffix);
 */