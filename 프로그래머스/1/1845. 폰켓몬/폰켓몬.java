import java.util.*;
class Solution {
    public int solution(int[] nums) {
//         int answer =0;
//         int get = nums.length /2 ;
        
//         HashSet <Integer> set = new HashSet <>();
        
//         for (int num : nums) {
//             set.add(num);
//         }
//         answer = Math.min(set.size(), get);
        
// 	    return answer;
//     }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    int answer = 0;
    int n = nums.length;
    int select_n = n/2;    
    
    HashSet <Integer> set = new HashSet<>();
        
    for (int num : nums) {
        set.add(num);
    }
        
    if (set.size() <= select_n) {
        answer = set.size();
    }else {
        answer = select_n;
    }
        
        
        
        
        
        
        
    return answer;
        
    }
}