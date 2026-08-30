import java.util.*;
class Solution {
    public String solution(String[] str_list, String ex) {

        
        StringBuilder sb = new StringBuilder();
        
        
        for (String s : str_list) {
            boolean is_ok = true;
            for (int i = 0; i<=s.length() - ex.length(); i ++)  { 
                String check =  s.substring(i, i +ex.length()) ;
                if (check.equals(ex)) {
                    is_ok = false;
                    break;
                }
            }
            
            if (!is_ok) {
                continue;
            }else {
                sb.append (s);
            }
        }
        
        return sb.toString();
        
    }
}