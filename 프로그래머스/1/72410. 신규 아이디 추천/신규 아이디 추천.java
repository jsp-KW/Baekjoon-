import java.util.*;
class Solution {
    public String solution(String new_id) {
        String answer = "";
        answer = new_id.toLowerCase(); // 치환 1단계
        answer = answer.replaceAll ("[^a-z0-9._-]", ""); //2 단계
        answer = answer.replaceAll("\\.{2,}", ".");//3 
        answer = answer.replaceAll("^\\.|\\.$", "");
        
        if(answer.isEmpty()) {
            answer= "a";
        }
        if (answer.length() >=16) {
            answer = answer.substring(0,15);
            if (answer.substring(answer.length()-1,answer.length()).equals(".")) { // java에서는 '' 랑 "" 랑 다르게 생각한다.
                answer= answer.substring(0,answer.length()-1);
            }
        }
        
        if (answer.length() <=2 )  {
            while (answer.length() != 3) {
                char last_ch = answer.charAt(answer.length() -1);
                answer = answer + last_ch;
            } 
        }
        
        
        return answer;
    }
}