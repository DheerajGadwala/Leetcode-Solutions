class Solution {
    
    List<List<Integer>> ans;
    
    public List<List<Integer>> combine(int n, int k) {
        this.ans = new ArrayList<>();
        res(n, k, new ArrayList<>());
        return ans;
    }
    
    private void res(int i, int k, List<Integer> acc) {
        if (k == 0) {
            ans.add(acc);
        }
        else if (i > 0) {
            List<Integer> copy = new ArrayList<>(acc);
            copy.add(i);
            res(i-1, k-1, copy);
            res(i-1, k, acc);
        }
    }
}