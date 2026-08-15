import java.util.*;
class Solution {
    int solution(int[][] land) {
        int answer = 0;

        int N = land.length;
        
        // dp 수식 정의하기
        // row, col
        // i번째 칸 , i-1번째의 칸의 col을 제외하고, 나머지 칸을 구하자
        // i-1번째 칸이 0,1,2,3 에서 0이면 1,2,3
        // 1이면  0,2,3 , 2면 0,1,3, 3이면 0,1,2
        
        // ANSWER N-1 행중에서 MAX 값
        int [][] dp = new int [N][4];
        dp[0][0] = land[0][0];
        dp[0][1] = land[0][1];
        dp[0][2] = land[0][2];
        dp[0][3] = land[0][3];
        
        
        for (int i =1; i<N; i++) {
            dp[i][0]  = Math.max(dp[i-1][1], Math.max(dp[i-1][2],dp[i-1][3])) + land[i][0];
            dp[i][1]  = Math.max (dp[i-1][0], Math.max(dp[i-1][2],dp[i-1][3]))  + land[i][1];
            dp[i][2]  = Math.max (dp[i-1][0], Math.max(dp[i-1][1],dp[i-1][3])) + land[i][2];
            dp[i][3]  = Math.max (dp[i-1][2], Math.max(dp[i-1][0],dp[i-1][1]))  + land[i][3];        
        }
                                  
        answer = -1;
        for (int i =0; i<4; i++) {
            if (dp[N-1][i] >= answer) {
                answer = dp[N-1][i];
            }
        }
        // 1행부터 N
        return answer;
    }
}