import java.util.*;

class Solution {
    public int solution(int[][] scores) {
        int answer = 0;
        
        int [] wanho = scores[0];
        int wanho_sum = wanho[0] +wanho[1];
        
        Arrays.sort(scores, (a,b) -> { 
            if (a[0] == b[0]) {
                return Integer.compare(a[1],b[1]);
            }
            return Integer.compare(b[0],a[0]);
        });
        
        
        int max_peer  = 0;
        int rank = 1;
        
        for (int [] score : scores)  {
            int att = score[0];
            int peer = score[1];
            
            if (peer < max_peer) {
                if (peer == wanho[1] && att == wanho[0])  {
                    return -1;
                } 
                continue;
            }
            
            max_peer = Math.max(max_peer, peer);
            
            if (wanho_sum < peer +att) {
                rank +=1;
            }  
        }
        return rank;
    }
}