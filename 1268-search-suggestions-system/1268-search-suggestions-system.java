class Solution {
    
    static class TrieNode {
        
        Map<Character, TrieNode> children;
        boolean endPoint;
        
        TrieNode() {
            children = new HashMap<>();
            endPoint = false;
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
    
    static class Trie {
        
        TrieNode head;
        
        Trie() {
            head = new TrieNode();
        }
        
        void add(String word) {
            
            TrieNode curr = head;
            for (char c: word.toCharArray()) {
                if (!curr.contains(c)) {
                    curr.add(c);
                }
                curr = curr.get(c);
            }
            curr.endPoint = true;
            
        }
        
        List<String> getSuggestions(String word) {
            
            TrieNode curr = head;
            for (char c: word.toCharArray()) {
                if (!curr.contains(c)) {
                    return new ArrayList<>();
                }
                else {
                    curr = curr.get(c);
                }
            }
            
            PriorityQueue<String> ret = new PriorityQueue<>();
            Map<TrieNode, String> map = new HashMap<>();
            Queue<TrieNode> q = new LinkedList<>();
            q.add(curr);
            map.put(curr, word);
            
            while (q.size() != 0) {
                TrieNode u = q.poll();
                if (u.endPoint) {
                    ret.add(map.get(u));
                }
                for (char c: u.children.keySet()) {
                    TrieNode v = u.get(c);
                    map.put(v, map.get(u) + c);
                    q.add(v);
                }
            }
            
            List<String> ans = new ArrayList<>();
            for (int i = 0; i < 3; i++) {
                if (ret.size() == 0) {
                    break;
                }
                else {
                    ans.add(ret.poll());
                }
            }
            
            return ans;
        }
    }
    
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Trie t = new Trie();
        for (String p: products) {
            t.add(p);
        }
        List<List<String>> ret = new ArrayList<>();
        String word = "";
        for (char c: searchWord.toCharArray()) {
            word += c;
            ret.add(t.getSuggestions(word));
        }
        return ret;
    }
}