import java.util.*;

class Solution {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        Queue <int[] > q = new ArrayDeque<>();
        
        q.offer (new int[] {0,0});
        
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            
            int idx = cur[0];
            int sum = cur[1];
            
            if (idx == numbers.length) {
                if (sum == target) {
                    answer +=1;
                }
                continue;
            }
            
            q.offer (new int [] {idx+1,sum + numbers[idx]});
            
            q.offer (new int [] {idx+1, sum -numbers[idx]});
            
            
        }
        
        return answer;
    }
}