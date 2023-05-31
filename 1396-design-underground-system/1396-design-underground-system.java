class UndergroundSystem {
    
    static class Pair {

        String from;
        String to;

        public Pair(String from, String to) {
            this.from = from;
            this.to = to;
        }

        @Override
        public int hashCode() {
            return Objects.hash(from, to);
        }
        
        @Override
        public boolean equals(Object thatObject) {
            Pair that = (Pair) thatObject;
            return that.from.equals(this.from) && that.to.equals(this.to); 
        }

    }
    
    Map<Pair, Double> totalTime;
    Map<Pair, Integer> totalCount;
    
    Map<Integer, Integer> checkinTime;
    Map<Integer, String> checkinStation;

    public UndergroundSystem() {
        totalTime = new HashMap<>();
        totalCount = new HashMap<>();
        checkinTime = new HashMap<>();
        checkinStation = new HashMap<>();
    }
    
    public void checkIn(int id, String stationName, int t) {
        checkinTime.put(id, t);
        checkinStation.put(id, stationName);
    }
    
    public void checkOut(int id, String stationName, int t) {
        
        String checkInStation = checkinStation.get(id);
        int checkInTime = checkinTime.get(id);
        
        Pair np = new Pair(checkInStation, stationName);
        
        if (!totalTime.containsKey(np)) {
            totalTime.put(np, 0.0);
            totalCount.put(np, 0);
        }
        
        totalTime.put(np, totalTime.get(np) + t - checkInTime);
        totalCount.put(np, totalCount.get(np) + 1);
    }
    
    public double getAverageTime(String startStation, String endStation) {
        Pair p = new Pair(startStation, endStation);
        
        return totalTime.get(p) / totalCount.get(p);
    }
}