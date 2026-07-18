import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue <Integer> pq = new PriorityQueue<>();
        for (int n : scoville) {
            pq.offer(n);
        }
        while ((pq.size() >=2) && (pq.peek() <K)) {
            int first = pq.poll();
            int second = pq.poll();
            int temp = first + (2*second);
            pq.offer(temp);
            answer+=1;
        }
        
        if (pq.peek() >= K) {
            return answer;
        }
        return -1;
       
        
    
  
    }
}