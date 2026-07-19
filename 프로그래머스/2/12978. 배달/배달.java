import java.util.*;
class Solution {
    public int solution(int N, int[][] road, int K) {

        
     
//         PriorityQueue <int [] > pq = new PriorityQueue<>((a,b) -> (a[0]-b[0]));
        

        
//         ArrayList <int[]> [] graph  = new ArrayList [N+1];
        
//         for (int i =0; i<N +1; i++) {
//             graph[i] = new ArrayList<>();
            
//         }
 
//         for (int [] r : road) {
//             int a = r[0];
//             int b = r[1];
//             int cost = r[2];
//             graph[a].add(new int [] {cost,b});
//             graph[b].add(new int [] {cost,a});
            
//         }

//         int [] distance = new int[N+1];
        
//         int INF = Integer.MAX_VALUE;
//         int start = 1;
//         Arrays.fill(distance, INF);
//         distance[1] = 0;
//         pq.offer (new int[] {0, 1});
        
//         while (!pq.isEmpty()) {
            
//             int [] get = pq.poll();
//             int cur_cost = get[0];
//             int cur_node = get[1];
            
//             if (cur_cost > distance[cur_node]) {
//                 continue;
//             }
            
//             for(int [] edge : graph[cur_node]) {
//                 int nxt_cost = edge[0];
//                 int nxt_node = edge[1];
                
//                 int total_cost = nxt_cost + distance[cur_node];
//                 if (total_cost <distance[nxt_node]) {
//                     distance[nxt_node] = total_cost;
//                     pq.offer (new int [] {total_cost, nxt_node});
//                 } 
//             }
            
//         }
        
//         for(int i =1; i< distance.length; i++) {
//             if (distance[i] <= K) {
//                 answer+=1;
//             }
//         }
        
        
        
        
        // K이하여야함
        // 마을 개수 N개
        // 음식 주문을 받을 수 있는 마을의 개수
        
        int answer = 0;
        
        ArrayList<int[]> [] graph = new ArrayList [N+1];
        
        for (int i =0;i<=N; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for (int [] r : road) {
            int start = r[0];
            int end = r[1];
            int cost = r[2];
            
            graph[start].add (new int [] {cost, end});
            graph[end].add(new int [] {cost, start});
            
        }
        
        PriorityQueue <int [] > pq = new PriorityQueue<>((a,b) -> Integer.compare (a[0],b[0]));
        int INF = Integer.MAX_VALUE;
        int distance[] = new int [N+1];
        int start = 1;
        
        Arrays.fill(distance, INF);
        distance[start] = 0;
        pq.offer (new int [] {0,1});
        
        while (!pq.isEmpty()) {
            int [] cur = pq.poll();
            int cur_cost = cur[0];
            int cur_node = cur[1];
            
            if (distance[cur_node] < cur_cost) {
                continue;
            }
            
            distance[cur_node] = cur_cost;
            for (int [] nxt : graph[cur_node]) {
                int nxt_cost = nxt[0];
                int nxt_node = nxt[1];
                
                if (distance[nxt_node] > nxt_cost + distance[cur_node]) {
                    int total_cost =  nxt_cost + distance[cur_node];
                    distance[nxt_node] = total_cost;
                    pq.offer(new int [] {total_cost, nxt_node});
                }
            }
        }
        
        for(int i =0; i<N+1; i++) {
            if( distance[i] <=K) {
                answer+=1;
            }
        }
        
        
        
        
        return answer;
    }
    

}