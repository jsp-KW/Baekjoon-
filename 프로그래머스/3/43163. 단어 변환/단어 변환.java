import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        
        ArrayDeque <String> q = new ArrayDeque<>();
        HashMap <String, Integer> hm = new HashMap<>();
        int n = words.length;
        boolean visited[] = new boolean[n];
        
        hm.put(begin, 0);
        q.offer(begin);
        
        
        while (!q.isEmpty()) {
            String cur_str = q.poll();
            
            if (cur_str.equals(target)) {
                break;
            }
            
            for (int i =0; i< words.length; i++) {
                String next_str = words[i];
                if (is_one_diff(cur_str, next_str)) {
                    if (!visited[i]) {
                        q.offer(next_str);
                        hm.put(next_str, hm.get(cur_str) +1);
                        visited[i] = true;
                    }
                }
            }
        }
        
        
        if (hm.containsKey(target)) {
            answer = hm.get(target);
        }else {
            return 0;
        }
        
    
        return answer;
    }
    
    private boolean is_one_diff (String str1, String str2) {
        char [] arr1 = str1.toCharArray();
        char [] arr2 = str2.toCharArray();
        int cnt = 0;
        for (int i =0; i< arr1.length; i++) {
            if (arr1[i] != arr2[i]) {
                cnt +=1;
            }
        }
        
        if (cnt >1) {
            return false;
        }
        if (cnt <=0) {
            return false;
        }
        
        return true;
    }
    
}