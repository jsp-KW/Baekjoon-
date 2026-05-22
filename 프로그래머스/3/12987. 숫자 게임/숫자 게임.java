import java.util.*;


class Solution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);
        
//         System.out.println(Arrays.toString(A));
        int answer =0;
        int i =0;
        int len = A.length;
        int temp_idx =0;
        while (i<A.length) {
            int target = A[i];
          
            while (temp_idx < B.length) {
                if (target < B[temp_idx]) {
                    answer +=1;
                    temp_idx = temp_idx+1;
                    break;
                }
                temp_idx +=1;
            }
            i+=1;
        }
      
        return answer;
    }
}