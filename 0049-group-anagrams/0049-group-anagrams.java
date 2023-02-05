class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Map<Character, Integer>, List<String>> groups = new HashMap<>();
        List<List<String>> ans = new ArrayList<>();
        for (String str: strs) {
            Map<Character, Integer> cnt = new HashMap<>();
            for (char c: str.toCharArray()) {
                cnt.put(c, cnt.getOrDefault(c, 0) + 1);
            }
            if (!groups.containsKey(cnt)) {
                groups.put(cnt, new ArrayList<>());
                ans.add(groups.get(cnt));
            }
            groups.get(cnt).add(str);
        }
        return ans;
    }
}