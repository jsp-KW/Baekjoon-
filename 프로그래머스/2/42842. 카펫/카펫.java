class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        
        // brown -6 한거의 위 아래 /2 
        // yellow는 
    
        // 전체 칸수는 brown + yellow 
        // brown = h-2 * 2 + 2w = 2w +2h -4
        // yellow = (w-2) 짜리가 h-2개 있음 = w-2 * h-2 = wh -2w -2h +4
        // 2w+2h -4 + wh -2w -2h +4 = wh
        // 
        
        int s = brown + yellow;
        
        for (int h=3; h<= Math.sqrt(s); h++) {
            if (s % h !=0) {
                continue;
            }
            
            int w = s / h;
            if ((w-2) * (h-2) == yellow) {
                return new int[] {w,h};

            }
            
        }
        return new int[] {0,0};
    }
}