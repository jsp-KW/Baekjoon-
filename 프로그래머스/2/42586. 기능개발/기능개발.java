import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        // 배포는 하루에 한번, 하루의 끝에 이어진다.
        int[] remains = new int[progresses.length];
        int [] days = new int [progresses.length];
        for (int i = 0; i< remains.length; i++) {
            remains[i] = 100 - progresses[i] ;
            if (remains[i] % speeds[i] == 0) { 
                days[i] = remains[i] / speeds[i];
            }else { 
                days[i] = (remains[i] / speeds[i]) +1;
            }
        }
        
        ArrayList <Integer>  arr = new ArrayList <>();
        
        int prev=  days[0];
        int cnt = 1;

        for (int i = 1; i < days.length; i++ )  {
            if (prev < days [i]) {
                arr.add (cnt);
                cnt =1;
                prev = days[i];
               
            }
            
            else if  (prev == days[i]) {
                cnt +=1;
            }
            else { 
                cnt +=1;
            }
        }
        
        arr.add(cnt);
        int [] answer = new int [arr.size()];
        int idx = 0;
        for (int num : arr) {
            answer [idx] = num;
            idx +=1;
        }
      
        return answer;
    }
}