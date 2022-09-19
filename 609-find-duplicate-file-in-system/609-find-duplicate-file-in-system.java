class Solution {
    public List<List<String>> findDuplicate(String[] paths) {
        Map<String, List<String>> groups = new HashMap<>();
        for (String path: paths) {
            String[] files = path.split(" ");
            for (int i = 1; i < files.length; i++) {
                String[] nc = files[i].split("[(]");
                if (!groups.containsKey(nc[1])) {
                    groups.put(nc[1], new ArrayList<>());
                }
                groups.get(nc[1]).add(files[0]+"/"+nc[0]);
            }
        }
        List<List<String>> ret = new ArrayList<>();
        for (List<String> l: groups.values()) {
            if (l.size() > 1) ret.add(l); 
        }
        return ret;
    }
}