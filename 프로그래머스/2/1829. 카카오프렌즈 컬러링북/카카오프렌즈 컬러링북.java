import java.util.*;
class Solution {
    
    boolean visited[][];
    public int[] solution(int m, int n, int[][] picture) {
        // 그림에 몇개의 영역이 있는지, 가장 큰 영역은 몇 칸으로 이루어져있는지 확인하기
        
        
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        
        HashSet <Integer> set = new HashSet<>();
        for (int i=0; i<m;i ++) {
            for (int j = 0; j<n; j++) {
                
                if (picture[i][j] ==0 ) {
                    continue;
                }
                set.add(picture[i][j]);
            }
        }
        
 
        
        visited =new boolean[m][n];
        
        
        for (int target :  set)  {
      
            for (int i = 0; i< m; i++ ) {
                for(int j = 0; j<n; j ++) {
                    if (picture[i][j] == target && !visited[i][j]) {
                        int result= bfs(picture,m,n, i,j, target);
                        maxSizeOfOneArea = Math.max(maxSizeOfOneArea, result);
                        numberOfArea ++;
                    }
                }
            }
     
            
            
        }


        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;

        
      
        
        return answer;
    }
    
    private int bfs (int [][] picture , int m, int n , int start_y, int start_x, int target) {
        
        int[] dy = {-1,1,0,0};
        int[] dx =  {0,0,-1,1};
        
        int cnt  =0;
        ArrayDeque<int []> q = new ArrayDeque<>();
        q.offer (new int [] {start_y, start_x});
        visited [start_y][start_x] = true;
        cnt =1;
            
        while (!q.isEmpty()) {
            int [] temp = q.poll();
            int cur_y  = temp[0];
            int cur_x  = temp[1];
            
            for (int i = 0; i<4; i ++ ) {
                int move_y = cur_y + dy[i];
                int move_x = cur_x + dx[i];
                
                if (0<= move_y && move_y <m && 0<=move_x && move_x < n) {
                    if (!visited[move_y][move_x] && picture[move_y][move_x] == picture[cur_y][cur_x]) {
                        q.offer (new int [] {move_y, move_x});
                        visited[move_y][move_x] = true;
                        cnt +=1;
                    }
                }
            }
            
        }
        
        return cnt;
    }
      
}