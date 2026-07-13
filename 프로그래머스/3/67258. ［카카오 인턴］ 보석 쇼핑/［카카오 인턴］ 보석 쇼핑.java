import java.util.*;

class Solution {
    public int[] solution(String[] gems) {
        int[] answer = {};
        HashMap<String, Integer> map = new HashMap<>();
        HashSet<String> set = new HashSet<>();
        
        
        for (String s : gems) {
            set.add(s);
        }
        
        int left = 0;
        int right = 0;
        int min_length = Integer.MAX_VALUE;
        int answer_left = 0;
        int answer_right = 0;
        
        while (right < gems.length) {
            // right +1
            String right_gem = gems[right];
            map.put(right_gem, map.getOrDefault(right_gem, 0) +1);
            
            while (map.size() == set.size())// 보석 종류가 다 찻다면, 계속해서 줄일 수 있는지 check, left +1
            {
                int cur_length = right - left +1;
                
                if (cur_length < min_length) {
                    min_length = cur_length;
                    answer_left = left;
                    answer_right = right;
                }
                String left_gem = gems[left];
                map.put(left_gem, map.get(left_gem)-1);
                
                if(map.get(left_gem)==0) {
                    map.remove(left_gem);
                }
                
                left ++;
            }
            
            right +=1;
            
            
        }
        
        
        return new int [] {answer_left +1, answer_right+1};
    }
}