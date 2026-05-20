import java.util.*;
class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        ArrayList <Integer>  li = new ArrayList <>();
        
        for (int s : score) {
            li.add (s);
        }
        
        Collections.sort (li, Collections.reverseOrder());
        int box_cnt = (score.length /m);
        int idx =0;
        
        while (box_cnt >0) {
            
           answer += (li.get (idx+m-1) * m);
           idx =idx +m;
            box_cnt -=1;
        }
        
        return answer;
    }
}