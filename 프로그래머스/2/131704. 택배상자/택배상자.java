import java.util.*;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        
        Stack <Integer> stack = new Stack<>();
        int check= 1;
        
        for (int target : order) {
            if ((!stack.isEmpty()) && (stack.peek() == target)) {
                    answer+=1;
                    stack.pop();
                    continue;
                }
        
  
                for (int i= check ; i <=target; i ++) {
                    stack.push(i);
                }
            
            check = target+ 1;
            
                
            
            if ((!stack.isEmpty() )&& stack.peek() == target) {
                answer +=1;
                stack.pop();
            }
            else break;
            
            
        }
        
        return answer;
            
        }
}
