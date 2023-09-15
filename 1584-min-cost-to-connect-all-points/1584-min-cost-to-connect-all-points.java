class Solution {
    
    // DisjoinSets data structure
    static class DisjointSets {
        
        Map<Pair, Pair> parent;
        int count; // count for number of nodes
        int sets; // count for number of sets
        
        DisjointSets() {
            parent = new HashMap<>();
            count = 0;
            sets = 0;
        }
        
        // make set
        void makeSet (Pair A) {
            parent.put(A, A);
            count++;
            sets++;
        } 
        
        // find operation
        Pair find (Pair A) {
            if (!parent.containsKey(A)) {
                makeSet(A);
                return A;
            }
            else if (parent.get(A).equals(A)) {
                return A;
            }
            else {
                parent.put(A, find(parent.get(A))); // reset parent
                sets--;
                return parent.get(A);
            }
        }
        
        // union
        boolean union(Edge e) {
            Pair Aparent = find(e.A);
            Pair Bparent = find(e.B);
            
            if (Aparent.equals(Bparent)) {
                return false;
            }
            else {
                parent.put(Bparent, Aparent);
                sets--;
                return true;
            }
        }
        
        
        
    }
    
    // Represents a node
    static class Pair {
        
        int x, y;
        
        Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }
        
        @Override
        public boolean equals(Object thatObject) {
            Pair that = (Pair) thatObject;
            return this.x == that.x && this.y == that.y;
        } 
    }
    
    // represents an edge
    static class Edge implements Comparable<Edge> {
        
        Pair A, B;
        int length;
        
        Edge(Pair A, Pair B) {
            this.A = A;
            this.B = B;
            this.length = Math.abs(A.x - B.x) + Math.abs(A.y - B.y); 
        }
        
        @Override
        public int compareTo(Edge that) {
            return Integer.compare(this.length, that.length);
        }
        
        
    }
    
    public int minCostConnectPoints(int[][] points) {
     
        List<Edge> allEdges = new ArrayList<>();
        
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                Pair A = new Pair(points[i][0], points[i][1]);
                Pair B = new Pair(points[j][0], points[j][1]);
                allEdges.add(new Edge(A, B));
            }
        }
        
        // Sort all edges
        Collections.sort(allEdges);
        
        DisjointSets ds = new DisjointSets();
        
        int ans = 0;
        
        // union find
        for (Edge e: allEdges) {
            
            if(ds.union(e)) {
                ans += e.length;
                if (ds.count == points.length && ds.sets == 1) {
                    break; // break when all nodes are in the set and there is only 1 set remaining
                }
            }
        }
        
        return ans;
    }
}