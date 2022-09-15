class Solution {
    public int[] findOriginalArray(int[] changed) {
        Map<Integer, Integer> count = new HashMap<>();
        Set<Integer> all = new TreeSet<>(), visited = new HashSet<>();
        for (int k: changed) {
            count.put(k, count.getOrDefault(k, 0) + 1);
            all.add(k);
        }
        List<Integer> ret = new ArrayList<>();
        for (int k: all) {
            if (count.getOrDefault(2*k, 0) < count.get(k)) return new int[0];
            if (k == 0 && count.get(k) % 2 == 1) return new int[0];
            else if (k == 0) count.put(k, count.get(k)/2);
            else count.put(2*k, count.getOrDefault(2*k, 0) - count.get(k));
            for (int i = 0; i < count.get(k); i++) ret.add(k);
        }
        int[] retArr = new int[ret.size()];
        for (int i = 0; i < ret.size(); i++) {
            retArr[i] = ret.get(i);
        }
        return retArr;
    }
}