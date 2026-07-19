import java.util.*;

class Solution {
    public String solution(int[] numbers) {
//         String answer = "";
//         // 정수를 이어붙여 만들수 있는 가장 큰 수
        
//         String [] nums = new String [numbers.length];
        
//         for (int i =0; i< numbers.length; i++) {
//             nums[i] = String.valueOf(numbers[i]);
//         }
        
//         //  compare (a,b) -> 값 양수인 경우  b a 순
//         //  음수인 경우 a b 순
//         //  0 이면 그대로
        
        
//         Arrays.sort (nums, (a,b)-> (b+a).compareTo(a+b)); // 610 > 106 -> 양수 리턴  a= 10 , b =6  ->즉  b a로 바뀜
        
//         if (nums[0].equals("0")) {
//             return "0";
//         }
        
        
//         StringBuilder sb = new StringBuilder ();
        
//         for (String s : nums) {
//             sb.append(s);
//         }
//         answer = sb.toString();
//         return answer;
        
      String answer = "";
      String [] nums = new String[numbers.length];
      for (int i =0; i< numbers.length; i++) {
          nums[i] = String.valueOf(numbers[i]);
      }  
        
      Arrays.sort (nums, (a,b)-> (b+a).compareTo(a+b));
      
      if (nums[0].equals("0")){
          return "0";
      }
        
      StringBuilder sb = new StringBuilder();
      for (String s : nums) {
          sb.append(s);
      }
        
    answer = sb.toString();
    return answer;
    }
    
}