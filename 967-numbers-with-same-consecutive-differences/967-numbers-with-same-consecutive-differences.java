class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
        
        Queue<Integer> q = new LinkedList<>();
        List<Integer> ans = new ArrayList<>();
        
        for (int i = 1; i < 10; i++) {
            q.add(i);
        }
        int last = (int)Math.pow(10, n - 1);
        while (q.size() != 0) {
            int u = q.poll();
            if (u >= last) {
                ans.add(u);
                continue;
            }
            if (u%10 + k < 10) {
                q.add(u * 10 + u % 10 + k);
            }
            if (k!= 0 && u%10 - k > -1) {
                q.add(u * 10 + u % 10 - k);
            }
        }
        
        int[] ret = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            ret[i] = ans.get(i);
        }
        return ret;
    }
}