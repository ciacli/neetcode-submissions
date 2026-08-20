class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int degs[] = new int[numCourses];
        List<List<Integer>> connections = new ArrayList<>();
        Queue<Integer> queue = new ArrayDeque<>();
        int count = 0;
        for(int i = 0; i < numCourses; ++ i){
            connections.add(new ArrayList<>());
        }
        for(int i = 0; i < prerequisites.length; ++ i){
            int before = prerequisites[i][0];
            int after = prerequisites[i][1];
            degs[after] ++;
            connections.get(before).add(after);
        }
        for(int i = 0; i < numCourses; ++ i) 
            if(degs[i] == 0) {
                queue.add(i);
                count ++;
            }
        while(queue.size() > 0){
            int head = queue.poll();
            for(int node : connections.get(head)){
                degs[node] --;
                if(degs[node] == 0) {
                    queue.add(node);
                    count ++;
                }
            }
        }
        return count == numCourses;

    }
}
