
import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
//       	boolean answer = true;
// 		HashMap <String, Integer> map = new HashMap<>();
		
// 		for(int i =0; i<phone_book.length; i++) {
// 			map.put(phone_book[i],i);
// 		}
		
// 		for(int i =0; i<phone_book.length; i++) {
// 			for(int k =1; k<phone_book[i].length(); k++) {
// 				if(map.containsKey(phone_book[i].substring(0,k)))
// 					return false;
// 			}
// 		}

        
        
        
       Arrays.sort(phone_book);
        
        for (int i = 1; i<phone_book.length; i ++) {
           if (phone_book[i].startsWith(phone_book[i-1])) {
               return false;
           }
        }
        
        
        return true;
    
        
          
        
    }
}