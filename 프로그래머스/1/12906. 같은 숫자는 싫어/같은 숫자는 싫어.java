import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
           int [] answer =null;
        
//         ArrayList<Integer> arr_list = new ArrayList<Integer>();
        
//         int value =-1;
        
//         for (int i =0; i<arr.length; i++) {
//             if (arr[i]!=value) {
//                 // 연속해서 같은 숫자가 아닐 경우에만 ArrayList에 저장한다. 
//                 arr_list.add(arr[i]);
//                 value = arr[i];
//             }
//         }
        
//         // ArrayList를 int형 배열로 바꾸기위해
//         // stream().mapToInt().toArray()를 이용.
//         return  arr_list.stream().mapToInt(i->i).toArray();
        
        
        
        ArrayList <Integer> li = new ArrayList <>();
        
        int prev = arr[0];
        for (int i =1; i< arr.length; i++) {
            if (prev != arr[i]) {
                li.add(prev);
                prev= arr[i];
            }
        }
        
        li.add(prev);
        answer = new int [li.size()];
        int idx= 0;
        
        for (int n : li) {
            answer[idx] = n;
            idx+=1;
        }
        return answer;
        
    }
}