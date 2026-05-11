import java.util.*;
class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int [score.length];
        
        PriorityQueue <Integer> pq = new PriorityQueue <>();
        int day = 1 ;
        int idx = 0;
        for (int s : score)  {
            if (day > k) {
                int cur_min = pq.peek();
                if (cur_min  < s) {
                    pq.poll();
                    pq.offer(s);
                }
            }else  {
                pq.offer(s);    
            }
            
            
            day +=1; 
            answer[idx] = pq.peek();
            idx+=1;
            
            
        }
        return answer;
    }
}