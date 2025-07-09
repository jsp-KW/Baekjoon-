import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        

        String [] str = new String[numbers.length];
        
        for (int i =0; i<str.length; i++) {
            str[i] = String.valueOf(numbers[i]);
        }
        
        
        Arrays.sort(str, new Comparator<String>(){
           @Override
            public int compare(String a, String b) {
                return(b+a).compareTo(a+b); // 내림차순 정렬 (o2+o1).compareTo(o1+o2); 
                                            //오름차순 정렬 (o1+o2).compareTo(o1+o2);
            }  // o2+o1이 o1+o2보다 클 경우 자리를 바꿔준다.
                
        });
        
        // 만약  0000000 이런 답이 나올경우.
        if(str[0].equals("0")) {
            answer +="0";
        }
        
        else {
            for (String s : str) 
                answer += s;
        }
        return answer;
    }
}