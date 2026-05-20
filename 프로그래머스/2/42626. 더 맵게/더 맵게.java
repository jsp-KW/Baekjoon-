import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue <Integer> pq = new PriorityQueue <>();
        
        for (int i=0; i<scoville.length; i++) {
            pq.offer (scoville[i]);
        }
        
        // offer 넣기 / poll 제일 작은 값 나옴
        
        //  최소힙의 루트가 k보다 작을때까지
        // 두개 배서 연산하고 결과값이 k보다 작을때까지?
        
        while  ((pq.size () >=2 ) && (pq.peek () < K)) {
            int num1 = pq.poll();
            int num2 = pq.poll();
            
            int scovill_res = num1  + (num2 *2);
            pq.offer (scovill_res);
            answer +=1;
        }
        
        // 더이상 섞지 못하는데 k보다 작은 경우
        
        if (pq.peek() <K)
            return  -1;
        
        return answer;
    }
}