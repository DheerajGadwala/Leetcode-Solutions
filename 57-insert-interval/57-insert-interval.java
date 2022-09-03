class Solution {
    public int[][] insert(int[][] in, int[] n) {
        List<Integer[]> intervals = new ArrayList<>();
        boolean flag = true, inserted = false;
        for (int[] i: in) {
            if (i[0] > n[1]) {
                if (flag) {
                    intervals.add(new Integer[] {n[0], n[1]});
                    flag = false;
                    inserted = true;
                }
                intervals.add(new Integer[] {i[0], i[1]});
            }
            else if (i[1] < n[0]) {
                intervals.add(new Integer[] {i[0], i[1]});
            }
            else {
                n[0] = Math.min(n[0], i[0]);
                n[1] = Math.max(n[1], i[1]);
                flag = true;
            }
        }
        if (!inserted) {
            intervals.add(new Integer[] {n[0], n[1]});
        }
        int[][] ret = new int[intervals.size()][2];
        for (int i = 0; i < intervals.size(); i++) {
            Integer[] it = intervals.get(i);
            ret[i] = new int[] {it[0], it[1]};
        }
        return ret;
    }
}