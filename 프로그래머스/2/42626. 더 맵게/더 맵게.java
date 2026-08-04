import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> Integer.compare(a,b));
        
        for (int num : scoville) {
            pq.offer(num);
        }
        
        while (pq.peek() <K && pq.size() >=2) {
            int num1 = pq.poll();
            int num2 = pq.poll();
            int temp = num1 + (num2 * 2);
            
            pq.offer(temp);
            answer+=1;
            
        }
        
        if (pq.peek() >= K) {
            return answer;
        }else {
            return -1;
        }
       
        
    
  
    }
}