class Solution {
    public record Tuple(int node, int time){}
    public int networkDelayTime(int[][] times, int n, int k) {
        int delays[] = new int[n];
        List<List<Tuple>> connections = new ArrayList<>(n);
        PriorityQueue<Tuple> queue = new PriorityQueue<Tuple>((a, b) -> Integer.compare(a.time, b.time));
        for(int i = 1; i <= n; ++ i){
            delays[i - 1] = -1;
            connections.add(new ArrayList<>());
        }
        for(int j = 0; j < times.length; ++ j){
            int start = times[j][0];
            int end = times[j][1];
            int time = times[j][2];
            connections.get(start - 1).add(new Tuple(end - 1, time));
        }
        delays[k - 1] = 0;
        queue.add(new Tuple(k - 1, 0));
        while(queue.size() > 0){
            Tuple head = queue.poll();
            int node = head.node;
            int delay = head.time;
            for(int i = 0; i < connections.get(node).size(); ++ i){
                Tuple connection = connections.get(node).get(i);
                if(delays[connection.node] == -1 || delays[connection.node] > delay + connection.time){
                    System.out.println(node + " " + connection.node + " " + delays[connection.node] + " " + (delay + connection.time)) ;
                    delays[connection.node] = delay + connection.time;
                    queue.add(new Tuple(connection.node, delays[connection.node]));
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < delays.length; ++ i){
            if(delays[i] == -1) return -1;
            ans = Math.max(ans, delays[i]);
        }
        return ans;
    }
}
