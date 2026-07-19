import java.util.*;
class Solution {
    public int[] solution(int n) {
//         int[] answer = {};
         
//         int [] dr = {1,0,-1};
//         int [] dc = {0,1,-1};
        
//         int [][] arr = new int [n][];
//         int num =1;
        
//         for (int i =0; i<n; i++) {
//             arr[i] = new int[i+1];
//         }
        
//         int direction_idx = 0;
//         int row =-1;
//         int col = 0;
//         // 0,0
//         // 1,0
//         // 2,0
//         // 3,0
        
//         for(int i =n ; i >=1 ; i = i-1) {
//             for (int j = 0; j< i; j++) {
//                 row = row +dr[direction_idx];
//                 col = col+ dc[direction_idx];
//                 arr[row][col] = num++;    
//             }
//             direction_idx = (direction_idx +1)%3;
//         }
        
//         ArrayList <Integer> li = new ArrayList <>();
        
//         int answer_idx = 0;
//         for (int i =0; i<n; i++) {
//             for (int j =0; j<=i; j++) {
//                 li.add(arr[i][j]);
//             }
//         }
//         answer = new int[li.size()];
//         for (int ans : li ){
//             answer[answer_idx++] = ans; 
//         }
        
        
        
        int [] answer= {};
        int [] dr = {1,0,-1};
        int [] dc = {0,1,-1};

        int [][] arr = new int [n][];
        int num =1;
        for (int i =0; i< n; i++) {
            arr[i] = new int[i+1];
        }
        
        int row = -1;
        int col = 0;
        
        int direction_idx = 0;
        for(int i = n; i>=1; i--) {
            for (int j = 0; j<i; j++) {
                row = row + dr[direction_idx];
                col = col +dc[direction_idx];
                arr[row][col] = num++;
            }
            direction_idx = (direction_idx +1)%3;
        }
        
        ArrayList<Integer> li = new ArrayList<>();
        
        for (int i =0; i<n; i++) {
            for (int j =0; j<i+1; j++) {
                li.add(arr[i][j]);
            }
        }
        answer = new int[li.size()];
        int idx =0;
        for (int t : li) {
         answer[idx++] = t;
           
        }
        return answer;
    }
}