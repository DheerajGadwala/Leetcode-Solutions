class Solution {
    public double champagneTower(int poured, int qi, int qj) {
        
        List<List<Double>> tower = new ArrayList<>();
        tower.add(new ArrayList<>());
        tower.get(0).add((double) poured);
        
        for (int i = 0; i < qi; i++) {
            tower.add(new ArrayList<>());
            tower.get(i + 1).add(0.0);
            for (int j = 0; j < i + 1; j ++) {
                
                int ci = i + 1;
                int lcj = j;
                int rcj = j + 1;
                
                double q = Math.max((tower.get(i).get(j) - 1) / 2, 0.0);
                
                tower.get(ci).set(lcj, tower.get(ci).get(lcj) + q);
                tower.get(ci).add(q);
            }
        }
        
        if (tower.get(qi).get(qj) > 1) {
            return 1.0;
        }
        else {
            return tower.get(qi).get(qj);
        }
        
    }
}