class DynamicArray {
    int[] array;
    int currPos, capacity;
    public DynamicArray(int capacity) {
        array = new int[capacity];
        this.capacity = capacity;
        currPos = 0;
    }

    public int get(int i) {
        return array[i];
    }

    public void set(int i, int n) {
        array[i] = n;
    }

    public void pushback(int n) {
        if(currPos == capacity) {
            resize();
        }
        array[currPos++] = n;

    }

    public int popback() {
        if(currPos > 0)
            return array[--currPos];
        else 
            return array[currPos];
    }

    private void resize() {
        int[] array1 = new int[capacity];
        for(int i = 0; i < currPos; ++ i)
            array1[i] = array[i];
        array = new int[capacity * 2];
        capacity *= 2; 
        for(int i = 0; i < currPos; ++ i)
            array[i] = array1[i];
        
    }

    public int getSize() {
        return currPos;
    }

    public int getCapacity() {
        return capacity;
    }
}
