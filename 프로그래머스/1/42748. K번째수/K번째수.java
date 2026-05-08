import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int [] answer  = new int [commands.length];
        // i~j까지 자르고 정렬했을때의 k번째에 있는 수
           
        int idx= 0;
        
        for (int[] com : commands) {
 
            int i = com[0]-1;
            int j = com[1];
            int k = com[2]-1;
            
            int[] temp = Arrays.copyOfRange (array ,i,j);
            Arrays.sort(temp);
            answer[idx] =temp[k];
            idx = idx +1;
        } 
        
         return answer;
              
    }
}

        
    


