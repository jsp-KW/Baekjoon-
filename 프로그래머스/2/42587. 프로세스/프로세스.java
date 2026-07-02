import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        // java로 mapping
        
        ArrayDeque <int[]> q = new ArrayDeque<>();
        int idx=0;
        for (int item : priorities) {
            int weight = item;
            q.offer (new int []{idx, weight});
            idx+=1;
        }
        
        
        while (true) {
            int [] target = q.poll();
            int target_idx = target[0];
            int target_weight = target[1];
            
            boolean check = true;
            for (int [] arr:  q) {
                
                int ch_index = arr[0];
                int ch_weight = arr[1];
                if (target_weight < ch_weight) {
                    check = false;
                    break;
                }
            }
            
            if (!check) {
                q.offer(new int[]{target_idx, target_weight});
            }
            else {
                answer+=1;
                if (target_idx == location) {
                    break;
                }
            }
            
        }
        return answer;
    }
}