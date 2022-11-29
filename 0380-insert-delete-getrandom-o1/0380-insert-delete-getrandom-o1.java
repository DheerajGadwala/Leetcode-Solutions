class RandomizedSet {

    Random rand;
    Map<Integer, Integer> positions;
    List<Integer> list;
    
    public RandomizedSet() {
        list = new ArrayList<>();
        positions = new HashMap<>();
        rand = new Random();
    }
    
    public boolean insert(int val) {
        if (positions.containsKey(val)) {
            return false;
        }
        list.add(val);
        positions.put(val, list.size()-1);
        return true;
    }
    
    public boolean remove(int val) {
        if (!positions.containsKey(val)) {
            return false;
        }
        int pos = positions.get(val);
        list.set(pos, list.get(list.size() - 1));
        positions.put(list.get(pos), pos);
        list.remove(list.size()-1);
        positions.remove(val);
        return true;
    }
    
    public int getRandom() {
        int r = rand.nextInt(list.size());
        return list.get(r);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */