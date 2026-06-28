import java.util.*;
class Solution {
    int answer =0;
    boolean[] visited;
    public int solution(int k, int[][] dungeons) {
        
        visited= new boolean [dungeons.length];
        
        dfs (k,dungeons,0);
        
        return answer;
    }
    
    public void dfs (int cur_hp, int[][] dungeons, int cnt) {
        answer = Math.max(cnt, answer);
        
        for (int i=0; i< dungeons.length; i++) {
            int need = dungeons[i][0];
            int cost = dungeons[i][1];
            
            if (!visited[i] && cur_hp >= need) {
                visited[i] = true;
                dfs (cur_hp - cost, dungeons, cnt+1);
                visited[i] = false;
            }
         
            
        }
    }
}