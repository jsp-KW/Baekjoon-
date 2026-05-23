import java.util.*;

class Solution {
    static Map<String, Integer> map;
    
    public String[] solution(String[] orders, int[] course) {
     
        ArrayList<String> answer = new ArrayList<>();
        
        for (int c: course) {
            map = new HashMap<>();
            
            
            for (String order : orders) {
                char [] ch_arr = order.toCharArray();
                Arrays.sort(ch_arr);
                
                combination(ch_arr,0,c,new StringBuilder());
            }
            
            int max_cnt = 0;
            
            for (int count : map.values()) {
                max_cnt = Math.max(max_cnt, count);
            }
            
            if (max_cnt <2) {
                continue;
            }
            
            
            for (String key: map.keySet()) {
                if(map.get(key)== max_cnt) {
                    answer.add(key);
                }
            }
            
            
        }
        
        Collections.sort(answer);
        return answer.toArray(new String[answer.size()]);
    }
    
    static void combination(char[] arr, int start, int targetLength, StringBuilder sb) {
        if(sb.length() == targetLength) {
            String menu = sb.toString();
            map.put(menu, map.getOrDefault(menu,0) +1);
            return;
        }
        
        for (int i =start; i <arr.length; i++) {
            sb.append(arr[i]);
            combination(arr,i+1,targetLength, sb) ;
            sb.deleteCharAt(sb.length()-1);
        }
    }
}