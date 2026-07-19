import java.util.*;

class Solution {
    public int[] solution(int n, int[][] roads, int[] sources, int destination) {
    
//         ArrayList<Integer> [] maps = new ArrayList [n+1] ;
        
//         for (int i =0; i <n+1 ; i++) {
//             maps[i] = new ArrayList<>();
//         }
        
//         for (int [] road : roads)  {
//             int a = road[0];
//             int b = road [1];
//             maps[a].add(b);
//             maps[b].add(a);
//         }
        
//         ArrayDeque <Integer> q = new ArrayDeque<>();
        
//         // destination -> 1 까지 bfs
//         q.offer(destination);
        
//         int [] distance = new int [n+1];
        
//         Arrays.fill(distance, -1);
//         distance [destination] = 0;
//         while (!q.isEmpty()) {
//             int cur = q.poll();
            
//             for(int nxt : maps[cur]) {
//                 if (distance[nxt] == -1)  {
//                     distance[nxt] = distance[cur] +1;
//                     q.offer (nxt);
//                 }
//             }
            
//         }
        
//         int [] answer = new int [sources.length];
//         int idx= 0;
        
//         // 답 저장하기
//         for (int target : sources) {
//             answer[idx] = distance[target];
//             idx = idx +1;
//         }
//         return answer;
   
        ArrayList<Integer> [] maps = new ArrayList[n+1];
        
        for (int i =0; i<= n; i ++) {
            maps[i] = new ArrayList<>();
            
        }
        
        for (int[] r : roads) {
            int start = r[0];
            int end = r[1];
            maps[start].add(end);
            maps[end].add(start);
        }
        
        
        ArrayDeque <Integer> q = new ArrayDeque<>();
        q.offer(destination);
        
        int distance[] = new int[n+1];
        Arrays.fill(distance, -1);
        distance[destination] = 0;
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for (int nxt : maps[cur]) {
                if (distance[nxt] ==-1) {
                    distance[nxt] = distance[cur] +1;
                    q.offer(nxt);
                }
            }
        }
        
        int [] answer = new int[sources.length];
        int idx= 0;
        for (int s : sources) {
            answer[idx] = distance[s];
            idx+=1;
        }
        
        return answer;
    }
}