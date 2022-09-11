class Solution {
    
    public static final int MOD = 1000000007;
    
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {    
        
        int[][] arr = new int[n][2];
        for(int i=0;i<n;i++) {
            arr[i][0]=efficiency[i];
            arr[i][1]=speed[i];
        }
        Arrays.sort(arr, (o1, o2) -> (o2[0] - o1[0]));
        
        PriorityQueue<Integer> q = new PriorityQueue<>();
        long sum = 0, ans = 0;
        for(int i = 0; i < n; i++) {
            sum += arr[i][1];
            q.add(arr[i][1]);
            if (q.size() > k) sum -= q.poll();
            ans = Math.max(ans,sum*arr[i][0]);
        }
        return (int) (ans % MOD);
    }
}