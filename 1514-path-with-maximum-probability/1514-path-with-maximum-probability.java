class Solution {
    public double maxProbability(int n, int[][] edges, double[] succProb, int start, int end) {
        
//          Dijkstra
        
        int m = edges.length;
        Map<Integer, Map<Integer, Double>> adj = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            adj.put(i, new HashMap<>());
        }
        
        for (int i = 0; i < m; i++) {
            int u = edges[i][0], v = edges[i][1];
            double prob = succProb[i];
            adj.get(u).put(v, Math.log(prob));
            adj.get(v).put(u, Math.log(prob));
        }
        
        double[] max = new double[n];
        for (int i = 0; i < n; i++) {
            max[i] = Double.NEGATIVE_INFINITY;
        }
        Queue<Integer> q = new LinkedList<>();
        max[start] = 0.0;
        q.add(start);
        
        while (q.size() != 0) {
            int u = q.poll();
            for (int v: adj.get(u).keySet()) {
                if (max[v] < max[u] + adj.get(u).get(v)) {
                    max[v] = max[u] + adj.get(u).get(v);
                    q.add(v);
                }
            }
        }
        
        return Math.pow(Math.E, max[end]);
        
        
//          Bellman-Ford
        
//         int m = edges.length;
//         Double[] max = new Double[n];
//         max[start] = 0.0;
        
//         for (int i = 0; i < m; i++) {
//             succProb[i] = Math.log(succProb[i]);
//         }
        
//         for (int i = 0; i < n; i++) {
//             for (int j = 0; j < m; j++) {
//                 int u = edges[j][0], v = edges[j][1];
//                 double prob = succProb[j];
//                 if (max[u] != null) {
//                     max[v] = max[v] == null? max[u] + prob : Math.max(max[v], max[u] + prob);
//                 }
//                 if (max[v] != null) {
//                     max[u] = max[u] == null? max[v] + prob : Math.max(max[u], max[v] + prob);
//                 }
//             }
//         }
//         return max[end] == null ? 0 : Math.pow(Math.E, max[end]);
    }
}