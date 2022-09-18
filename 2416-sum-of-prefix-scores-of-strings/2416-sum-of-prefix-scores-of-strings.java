class Solution {
    
    // TrieNode
    static class Node {
        Map<Character, Node> children;
        int count;
        Node() {
            children = new HashMap<>();
            count = 0;
        }
        boolean contains(char c) {
            return children.containsKey(c);
        }
    }
    
    public int[] sumPrefixScores(String[] words) {
        Node root = new Node();
        // add words to Trie and update counts
        for(String word: words) {
            Node curr = root;
            for (char c: word.toCharArray()) {
                if (!curr.contains(c)) {
                    curr.children.put(c, new Node());
                }
                curr = curr.children.get(c);
                curr.count += 1;
            }
        }
        int[] ret = new int[words.length];
        // find answer for the ith word
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            int cnt = 0;
            Node curr = root;
            for (char c: word.toCharArray()) {
                if (curr.contains(c)) {
                    curr = curr.children.get(c);
                    cnt += curr.count;
                }
                else {
                    break;
                }
            }
            ret[i] = cnt;
        }
        return ret;
    }
}