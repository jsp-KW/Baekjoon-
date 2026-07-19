import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
//         // java로 mapping
        
//         ArrayDeque <int[]> q = new ArrayDeque<>();
//         int idx=0;
//         for (int item : priorities) {
//             int weight = item;
//             q.offer (new int []{idx, weight});
//             idx+=1;
//         }
        
        
//         while (true) {
//             int [] target = q.poll();
//             int target_idx = target[0];
//             int target_weight = target[1];
            
//             boolean check = true;
//             for (int [] arr:  q) {
                
//                 int ch_index = arr[0];
//                 int ch_weight = arr[1];
//                 if (target_weight < ch_weight) {
//                     check = false;
//                     break;
//                 }
//             }
            
//             if (!check) {
//                 q.offer(new int[]{target_idx, target_weight});
//             }
//             else {
//                 answer+=1;
//                 if (target_idx == location) {
//                     break;
//                 }
//             }
            
//         }
        
        ArrayDeque <int []> q = new ArrayDeque<>();
        
        for (int i=0; i< priorities.length; i++) {
            q.offer(new int[] {i, priorities[i]});
        }
        
        while (true) {
            int [] cur = q.poll();
            int cur_idx = cur[0];
            int cur_weight =cur[1];
            
            boolean check = true;
            
            for(int [] temp : q) {
                int temp_weight = temp[1];
                
                if (temp_weight > cur_weight) {
                    check = false;
                    break;
                }
            }
            
            if(!check)  {
                q.offer(new int [] {cur_idx, cur_weight});
            }
            else{
                answer+=1;
                if (location == cur_idx) {
                    break;
                }
            }
            
        }
        
        return answer;
    }
}