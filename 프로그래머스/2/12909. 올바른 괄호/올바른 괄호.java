import java.util.*;
class Solution {
    boolean solution(String s) {
        boolean answer = true;

       Stack <Character> stack = new Stack<>();
        
        for (int i= 0; i <s.length(); i ++) {
            char  target = s.charAt(i);
            
            if (target == '(') {
                stack.push (target);
            }
            else {
                if (stack.isEmpty()){
                    answer = false;
                }else {
                    if (stack.peek () == '(') {
                        stack.pop();
                    }  else {
                        answer = false;
                    }
                }
            }
        }
        
        if (! stack.isEmpty()) {
            answer = false;
        }
        
        
        return answer;
        
        
        
        

    }
}