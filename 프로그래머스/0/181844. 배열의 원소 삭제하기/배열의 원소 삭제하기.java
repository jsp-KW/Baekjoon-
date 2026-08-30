import java.util.*;


class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        int[] answer = {};
        
        ArrayList<Integer> li = new ArrayList<>();
    
        ArrayList<Integer> remove_li = new ArrayList<>();
        for (int t : delete_list) {
            remove_li.add(t);
        }
        
        for (int n : arr) {
            if (remove_li.contains(n)) {
                continue;
            }else {
                li.add(n);
            }
        }
        
        int idx = 0; 
        answer = new int [li.size()];
        
        for (int get_num : li ) { 
            answer[idx++] = get_num;
        }
        
        return answer;
    }
}