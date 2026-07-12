import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        // 10개 받음 / 3개 줌 : 선물지수 = 준거 - 받은거 =  -7
        // A와 B가 선물을 주고받은 적이 없거나, 정확히 같은 수로 선물을 주고 받았다면 -> B가 A에게 선물을 받는다
        // 선물 지수가 같다면 다음 달에 선물을 주고 받지 않는다.
        
        // 선물지수 작은 사람 ->> 선물지수 큰 사람한테 기부
        
        
        // 다음 달에 가장 많은 선물을 받는 친구가 받을 선물의 수를 RETURN
        // gifts[] = A 선물 준 친구 / B 선물을 받은 친구  공백으로 기준
        
        HashMap <String, HashMap <String,Integer>> give_map = new HashMap<>();
        HashMap <String, HashMap <String,Integer>>  get_map = new HashMap<>();
        
        for (String info : gifts ) {
            String[] temp = info.split(" ");
            String A = temp[0];
            String B = temp[1];
            
            if (!give_map.containsKey(A)) {
                give_map.put(A, new HashMap<>());
                
            }
            
            HashMap <String, Integer> give_inner_map = give_map.get(A);
            give_inner_map.put(B, give_inner_map.getOrDefault(B,0) +1);
            
            if (!get_map.containsKey(B)) {
                get_map.put(B, new HashMap<>());
            }
            HashMap<String, Integer> get_inner_map = get_map.get(B);
            get_inner_map.put(A, get_inner_map.getOrDefault(A,0) +1);
            
            
        }

        
        HashMap<String, Integer> gift_score=  new HashMap<>();
        
        // 선물 지수 계산
        
        for (String friend : friends) {
            int give_cnt = 0;
            int get_cnt = 0;
            
            if (give_map.containsKey(friend)) {
                HashMap<String, Integer> give_inner_map = give_map.get(friend);
                
                
                for (int count : give_inner_map.values()) {
                    give_cnt += count;
                }
                    
            }
            
            if (get_map.containsKey(friend)) {
                HashMap<String, Integer> get_inner_map = get_map.get(friend);
                
                for(int count : get_inner_map.values()) {
                    get_cnt += count;
                }
            }
            
            gift_score.put(friend, give_cnt - get_cnt);
        }

        
        
        
        // 다음달에 받을 개수 
        
        HashMap<String, Integer> next_gift=  new HashMap<>();
        
        for(String friend:  friends) {
            next_gift.put(friend,0);
        }
        
        for (int i =0; i<friends.length; i++) {
            for (int j = i+1; j <friends.length; j++) {
                String A = friends[i];
                String B = friends[j];
                
                // A->B 에게 준 수
                int A_to_B =  0;
                
                
                // B->A 에게 준 수
                int B_to_A = 0;
                
                
                if (give_map.containsKey(A)) {
                    A_to_B = give_map.get(A).getOrDefault(B,0);
                }
                
                if (give_map.containsKey(B)) {
                    B_to_A = give_map.get(B).getOrDefault(A,0);
                }
                
                if (A_to_B == B_to_A) {
                    
                    if (gift_score.get(A) > gift_score.get(B)) {
                        next_gift.put(A, next_gift.get(A)+1);
                    }else if (gift_score.get(A) < gift_score.get(B)) {
                        next_gift.put(B, next_gift.get(B) +1);
                    }
                    
                } else if (A_to_B > B_to_A) {
                    
                    next_gift.put(A, next_gift.get(A)+1);
                    
                }else {
                    next_gift.put(B, next_gift.get(B) +1);
                }
                
            }
        }
        
        
        for (int n : next_gift.values()) {
            answer = Math.max(answer, n);
        }
        
        
        return answer;
    }
}