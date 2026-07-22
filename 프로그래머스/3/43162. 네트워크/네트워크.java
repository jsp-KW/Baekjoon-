import java.util.*;
class Solution {
    
    int visited[];
    public int solution(int n, int[][] computers) {
   
        int[][] coms = computers;
        int answer = 0;
        int network_num =1;
        visited  = new int [n];
        
        for (int i =0; i<n; i++) {
            if (visited[i] ==0) {
                bfs(i,network_num,coms);
                network_num+=1;
                answer+=1;
            }
        }
        
        
 
        return answer;
    }
    
    private void bfs( int start,int network_num, int[][] computers) {
        ArrayDeque <Integer> q = new ArrayDeque<>();
        q.offer(start);
        visited[start] = network_num;
 
          
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for(int i =0 ;i< computers[cur].length; i++) {
                if (visited[i] == 0 && computers[cur][i] ==1) {
                    visited[i] = network_num;
                    q.offer(i);
                }
            }
            
            
        }
  
        
    } 
}