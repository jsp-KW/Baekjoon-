import java.util.*;

class Solution {
    
     int sheep = 1;
     int wolf = 0;
    int answer =0;
    public int solution(int[] info, int[][] edges) {
   
        int n = info.length;
        ArrayList<Integer> []tree  = new ArrayList[n];
        
        for (int i= 0; i< n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int [] temp : edges) {
            int start = temp[0];
            int end = temp[1];
            tree[start].add(end);
        }
        ArrayList<Integer> candidates = new ArrayList<>();
        candidates.addAll(tree[0]);
        
        dfs(1,0,candidates, tree, info);
        
        return answer;
    }
    
    void dfs (int sheep, int wolf, ArrayList<Integer> candidates, ArrayList<Integer> [] tree, int[]info) {
        
        answer = Math.max(answer, sheep);
        
        for (int nxt : candidates) {
            int next_sheep = sheep;
            int next_wolf = wolf;
            
            if (info[nxt] == 1)
                next_wolf +=1;
            
            if (info[nxt]==0)
                next_sheep +=1;
            
            if (next_sheep <= next_wolf) 
                continue;
            
            ArrayList<Integer> next_candidates = new ArrayList<>(candidates);
            next_candidates.remove(Integer.valueOf(nxt));
            
            for (int nxt_node : tree[nxt]) {
                next_candidates.add(nxt_node);
            } 
            
            dfs (next_sheep, next_wolf, next_candidates, tree, info);
        }
        
        
    }
    
    
}