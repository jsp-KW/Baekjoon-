import java.util.*;

class Solution {
    public int solution(int n, int[][] costs) {
        
        ArrayList<int[]>[] graph = new ArrayList [n];
        for (int i =0; i<n; i++) {
            graph[i] = new ArrayList<>();
        }
        
        for(int [] item: costs) {
            int start = item[0];
            int end = item[1];
            int cost = item[2];
            
            graph[start].add(new int [] {cost,end});
            graph[end].add(new int [] {cost,start});
            
        }
        
        
        PriorityQueue <int []> q = new PriorityQueue <>((a,b) -> a[0] -b[0]);
        
        q.offer(new int[] {0,0});
        int cnt = 0;
        int answer =0;
        
        boolean[] visited = new boolean[n];
        int total_cost = 0;
        Arrays.fill(visited, false);
        while (!q.isEmpty()) {
            int []item = q.poll();            
            int cur_cost =  item[0];
            int cur_node =  item[1];
            
            if(visited[cur_node]) {
               continue; 
            }
            
         
            
            visited[cur_node] = true;
            total_cost = total_cost + cur_cost;
            cnt+=1;
            
            if (cnt == n) {
                answer = total_cost;
                break;
            }
            for (int [] nxt : graph[cur_node]) {
                int nxt_cost = nxt[0];
                int nxt_node = nxt[1];
                
                if (!visited[nxt_node]) {
                    q.offer (new int [] {nxt_cost, nxt_node});
                }
            }
            
        }
        
        return answer;
        
    }
}