import java.util.*;

class Solution {
     
    int [] dy = {-1,1,0,0};
    int [] dx= {0,0,-1,1};
    int answer =0;
    
    public int solution(String[] board) {

        int row= board.length;
        int col= board[0].length();
        int [][] distance = new int [row][col];
        char [][] maps=  new char [row][col];
        
        for (int i=0; i< row; i++) {
            maps[i] = board[i].toCharArray(); // 이게 삽입됨? 되네
        }

        // cur_y, cur_x // next_y, next_x 다음꺼가 D거나 범위를 벗어나는 경우 방향을 바꿔서 이동
        
        for(int [] temp : distance) {
            Arrays.fill (temp, -1);
        }
        
        ArrayDeque <int []> q = new ArrayDeque<>();
        int start_y = 0;
        int start_x = 0;
        
        
        for (int i=0; i< row; i++) {
            for (int j =0; j<col; j++) {
                if (maps[i][j] == 'R') {
                    start_y = i;
                    start_x = j;
                    break;
                }
            }
        }
        distance[start_y][start_x] = 0;
        q.offer(new int [] {start_y, start_x});
        
        while (!q.isEmpty()) {

            int[] cur_cord= q.poll();
            int cur_y =cur_cord[0];
            int cur_x = cur_cord[1];
            
                
            if (maps[cur_y][cur_x] == 'G') {
                return distance[cur_y][cur_x];
            }
            
            for (int i =0; i<4; i++) {
                int next_y = cur_y;
                int next_x = cur_x;
            
            
                while (true) {
                    int test_y = next_y +dy[i];
                    int test_x = next_x + dx[i];

                    if (0>test_y || test_y >= row || test_x <0 || test_x >=col || maps[test_y][test_x] =='D') { //범위 밖이라면
                        break;                  
                    }

                    next_y = test_y;
                    next_x = test_x;

                }

                // 방문처리

                if (distance[next_y][next_x] == -1) {
                    distance[next_y][next_x] = distance[cur_y][cur_x] + 1;
                    q.offer(new int[] {next_y, next_x});
                }

        }
    }
       
        return -1;
    }

}