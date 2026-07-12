import java.util.*;

class Solution {
    public int solution(int[][] signals) {
        int answer = 0;
        
        int total_cycle = 1;
        for (int i =0; i<signals.length; i++ ) {
            int g = signals[i][0];
            int y = signals[i][1];
            int r = signals[i][2];
            
            
            int total = r+y+g;
            
            total_cycle = lcm(total_cycle, total);
            
        }
        
        
    
        
        for (int time=1; time <= total_cycle; time++) {
            
            boolean all_yellow = true;
            for(int[] signal: signals) {
                if (!isYellow(time,signal)) {
                    all_yellow = false;
                    break;
                }
            }
            
            
            if (all_yellow) {
                return time;
            }
            
            
        }
        
        
        return -1;
        
    }
    
    private boolean isYellow(int time, int [] signal) {
        int G = signal[0];
        int Y = signal[1];
        int R = signal[2];
        
        int cycle = G+Y+R;
        int remain = time % cycle;
        
        return remain >G && remain <= G+Y;
    }
    
    private int gcd(int a, int b) {
        while (b!=0) {
            int temp = a%b;
            a= b;
            b = temp;
        }
        
        return a;
    }
    
    private int lcm(int a , int b) {
        
        if (gcd(a,b) ==0) {
            return 0;
        } 
        
        int result =  (a*b) / gcd(a,b);
        return result;
    }
    
    
    
    
}