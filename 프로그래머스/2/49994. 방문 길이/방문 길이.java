import java.util.*;
class Solution {
    public int solution(String dirs) {
        int answer = 0;
        HashSet <String> hs = new HashSet <>();
        
        int cur_y =0;
        int cur_x =0;
    
        for (int i=0; i< dirs.length(); i ++) {
            char dir = dirs.charAt(i);
            
            int next_y =cur_y;
            int next_x = cur_x;
            
            if (dir=='L') next_x-=1;
            else if (dir=='R') next_x +=1;
            else if (dir=='U') next_y +=1;
            else next_y -=1;
            
            if (!check(next_y,next_x)) continue;
            
            String path = next_y +","+next_x+","+cur_y+","+cur_x;
            String reverse =cur_y+","+cur_x+","+next_y+","+next_x;
            hs.add(path);
            hs.add(reverse);
            
            cur_y = next_y;
            cur_x = next_x;
        
        }
        
        
        answer = hs.size() /2 ;
        
        
        return answer;
    }
    
    public static boolean check(int y, int x) {
        if ((-5 <= x &&  x<=5 )&& (-5 <= y && y<= 5) )
            return true;
        else
            return false ;
    } 
}