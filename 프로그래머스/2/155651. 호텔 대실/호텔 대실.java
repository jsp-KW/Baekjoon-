import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        
        int[][] times = new int [book_time.length][2];
        
        int idx= 0;
        
        for (String [] target : book_time) {
            int start_h = Integer.parseInt(target[0].substring(0,2)) * 60;
            int start_m = Integer.parseInt(target[0].substring(3,5));
            
            int end_h = Integer.parseInt(target[1].substring(0,2))*60;
            int end_m = Integer.parseInt(target[1].substring(3,5)) +10;
            
            int s = start_h+start_m;
            int e = end_h +end_m;
            
            times[idx][0] = s;
            times[idx][1] =e;
            idx +=1;
            
        }
        
        Arrays.sort (times, (a,b) -> a[0]-b[0]);
        
//         for (int[] a : times) {
//              System.out.println(Arrays.toString(a));
//         }
        
        PriorityQueue <Integer> pq = new PriorityQueue<>();
        
        for (int [] target : times ) {
            int start = target[0];
            int end = target[1];
            
            if (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll(); 
            }else {
                answer+=1;
            }
            pq.offer (end);

        }
       
        return answer;
    }
}