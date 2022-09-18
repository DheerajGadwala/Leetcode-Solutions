class Solution {
    
    // TrieNode
    static class Node {
        Map<Character, Node> children;
        Map<Character, Integer> count;
        Node() {
            children = new HashMap<>();
            count = new HashMap<>();
        }
        boolean contains(char c) {
            return count.containsKey(c);
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
                    curr.count.put(c, 0);
                }
                curr.count.put(c, curr.count.get(c) + 1);
                curr = curr.children.get(c);
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
                    cnt += curr.count.get(c);
                    curr = curr.children.get(c);
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