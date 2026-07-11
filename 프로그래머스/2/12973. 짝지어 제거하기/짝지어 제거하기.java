import java.util.*;
class Solution
{
    public int solution(String s)
    {
        int result = 0;   
        char [] ch_arr = s.toCharArray();
        Stack <Character> stack = new Stack<>();
        
        for (int i =0; i< ch_arr.length; i++) {
            char ch = ch_arr[i];
            
            if (stack.isEmpty()) {
                stack.push(ch);
            }else {
                if (stack.peek() == ch) {
                    stack.pop();
                }else {
                    stack.push(ch);
                }
            }
        } 
        
        if (stack.isEmpty()) {
            result = 1;
        }else {
            result = 0;
        }
    
        return result;
    }
}
