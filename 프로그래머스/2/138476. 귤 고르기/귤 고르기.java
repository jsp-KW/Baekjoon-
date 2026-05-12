import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        HashMap <Integer, Integer>  map = new HashMap <>();
        
        for(int  t : tangerine) {
            if (!map.containsKey(t))  {
                map.put(t, 1);
            }else {
                map.put(t, map.get(t)+1);
            }
        }
        
        ArrayList <Integer> arr_li = new ArrayList <>(map.values());
        
        arr_li.sort (Collections.reverseOrder());
        int cur_cnt  = 0;
        int type_cnt = 0;
        
        for (int cnt : arr_li) {
            if (cur_cnt  >= k) {
                break;
            } 
            
            cur_cnt += cnt ;
            type_cnt +=1; 
        
        }
        answer = type_cnt;
        
        return answer;
        
    }
}