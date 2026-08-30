import java.util.*;
import java.util.*;
class Solution {
    public int solution(String[] strArr) {
        int answer = -1;
        
        HashMap <Integer, Integer> hm = new HashMap <>();
        
        for (String s : strArr) {
            if (hm.containsKey(s.length())) {
                hm.put (s.length(), hm.get(s.length()) +1);
            }else {
                hm.put(s.length(),  1);
            }
        }
        
        
        for (int num : hm.values()) {
            answer = Math.max(answer, num);
        }
        
        return answer;
    }
}