import java.util.*;
class Solution {
    public int solution(int[][] maps) {
//         int n = maps.length;
//         int m = maps[0].length;
        
//         int answer = 0;
        
//         boolean [][] visited = new boolean[n][m];
//         int [][] distance = new int [n][m];
//         int [] dy =  {-1,1,0,0};
//         int [] dx = {0,0,-1,1};
//         ArrayDeque <int[]> q= new ArrayDeque <>();
        
//         q.offer(new int [] {0,0});
//         visited[0][0] = true; 
//         distance[0][0] = 1;
//         while (!q.isEmpty()) {
//             int [] cur = q.poll();
            
//             int cur_y = cur[0];
//             int cur_x = cur[1];
            
//             for (int i =0; i<4; i++) {
//                 int my = cur_y +dy[i];
//                 int mx = cur_x +dx[i];
                
//                 if( (0 <= my && my <n ) && (0<= mx && mx <m)) {
//                     if( (!visited[my][mx]) && (maps[my][mx] ==1) ) {
//                         q.offer (new int [] {my,mx});
//                         visited[my][mx] = true;
//                         distance[my][mx] = distance[cur_y][cur_x] +1;
//                     }
//                 }
//             }
//         }
        
//         if (distance[n-1][m-1] == 0 ) {
//             return -1;
//         }
        
//         answer = distance[n-1][m-1];
        
        
        
        int row = maps.length;
        int col = maps[0].length;
        
        int answer = 0;
        
        int distance [][] = new int [row][col];
        ArrayDeque <int []> q = new ArrayDeque<>();
        
        
        int dy[] = {-1,1,0,0};
        int dx[] = {0,0,-1,1};
        
        
        for (int i =0; i< row; i++) {
            for (int j =0; j<col; j++) {
                distance[i][j] = -1;
            }
        }
       
        
        q.offer(new int[] {0,0});
        distance[0][0] = 1;
        while (!q.isEmpty()) {
            int [] target = q.poll();
            int cur_y = target[0];
            int cur_x = target[1];
           
            for (int i =0; i<4; i++) {
                int move_y = cur_y + dy[i];
                int move_x = cur_x + dx[i];
                
                if( (0<=move_y && move_y < row) && (0<= move_x && move_x <col)) {
                    if (maps[move_y][move_x] ==1 && distance[move_y][move_x] ==-1) {
                        distance[move_y][move_x] = distance[cur_y][cur_x] +1;
                        q.offer(new int [] {move_y, move_x});
                    }
                }
            }
            
        
        }
        
        answer = distance[row-1][col-1];
      
    
        return answer;
    }
}