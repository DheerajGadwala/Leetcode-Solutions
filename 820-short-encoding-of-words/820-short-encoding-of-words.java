class Solution {
    
    class TrieNode {
        
        boolean endPoint;
        Map<Character, TrieNode> children;
        
        TrieNode() {
            endPoint = false;
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
    
    class Trie {
        
        TrieNode head;
        
        Trie() {
            head = new TrieNode();
        }
        
        void addRev(String word) {
            TrieNode curr = head;
            for (int i = word.length() - 1; i > -1; i--) {
                char c = word.charAt(i);
                if (!curr.contains(c)) {
                    curr.add(c);
                }
                curr = curr.get(c);
            }
            curr.endPoint = true;
        }
        
        int getAns() {
            int ans = 0;
            Queue<TrieNode> q = new LinkedList<>();
            Map<TrieNode, Integer> length = new HashMap<>();
            q.add(head);
            length.put(head, 1);
            while (q.size() != 0) {
                TrieNode u = q.poll();
                if (u.children.size() == 0) {
                    ans += length.get(u);
                }
                for (char c: u.children.keySet()) {
                    TrieNode v = u.get(c);
                    q.add(v);
                    length.put(v, length.get(u) + 1);
                }
            }
            return ans;
        }
        
    }
    
    public int minimumLengthEncoding(String[] words) {
        Trie t = new Trie();
        for (String word: words) {
            t.addRev(word);
        }
        return t.getAns();
    }
}