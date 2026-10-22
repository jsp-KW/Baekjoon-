import java.util.*;

class Solution {
    char[] friends = {'A', 'C', 'F', 'J', 'M', 'N', 'R', 'T'};
    boolean[] visited = new boolean[8];
    int answer = 0; // 전역 변수(필드)로 빼서 관리

    // 1. 시작점
    public int solution(int n, String[] data) {
        answer = 0; // 테스트 케이스마다 초기화
        visited = new boolean[8]; // 방문 배열도 초기화
        dfs("", data);
        return answer;
    }
    
    // 2. DFS (줄 세우기 공장)
    public void dfs(String cur, String[] data) {
        // 8명이 모두 줄을 섰다면 조건 검사하러
        if (cur.length() == 8) {
            if (check(cur, data)) {
                answer++;
            }
            return;
        }
        
        // 8명을 순서대로 하나씩 뽑아서 줄에 세움
        for (int i = 0; i < 8; i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(cur + friends[i], data); // 다음 사람 세우러 재귀 호출
                visited[i] = false; // 백트래킹 (원상복구)
            }
        }
    }
    
    // 3. 조건 심사관 (만들어진 줄이 조건을 다 만족하는지 검사)
    public boolean check(String cur, String[] data) {
        for (String cond : data) {
            char p1 = cond.charAt(0);
            char p2 = cond.charAt(2);
            char op = cond.charAt(3);
            int targetDist = cond.charAt(4) - '0';
            
            int idx1 = cur.indexOf(p1);
            int idx2 = cur.indexOf(p2);
            int actualDist = Math.abs(idx1 - idx2) - 1; // 실제 사이에 낀 사람 수
            
            if (op == '=') {
                if (actualDist != targetDist) return false;
            } else if (op == '>') {
                if (actualDist <= targetDist) return false;
            } else if (op == '<') {
                if (actualDist >= targetDist) return false;
            }
        }
        return true; // 모든 조건을 통과함!
    }
}