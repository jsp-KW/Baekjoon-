import java.util.*;
class Solution {
    int [] selected;
    int [] answer= {0,0};
    int [] sales = {10,20,30,40};
    
    void make_sale_dfs (int depth, int[][] users, int [] emoticons) {
        if (depth == emoticons.length) {
            calculate (users, emoticons);
            return;
        }
        
        for (int sale: sales) {
            selected[depth] = sale;
            make_sale_dfs(depth+1, users, emoticons);
        }
        
    }
    
    void calculate (int[][] users, int[] emoticons) {
        int plus_count = 0;
        int total_price =0;
        
        for (int [] user: users) {
            int userSale = user[0];
            int userLimit = user[1];
            
            int userPrice = 0;
            
            for (int i=0; i< emoticons.length; i++) {
                int sale = selected[i];
                
                if (sale>= userSale) {
                    userPrice +=  (emoticons[i]*(100-sale))/100;
                    
                }
            }
            
            if (userPrice >= userLimit) {
                plus_count +=1;
            }else {
                total_price += userPrice;
            }
            
         
        }
        if (answer[0] <plus_count) {
            answer[0] = plus_count;
            answer[1] = total_price;
        }
        else if((answer[0] == plus_count) && (answer[1] < total_price)) {
            answer[1] = total_price;
        }
    }
    
    
    public int[] solution(int[][] users, int[] emoticons) {
        
        selected = new int [emoticons.length];
        make_sale_dfs (0,users,emoticons);
        
        
        return answer;
    }
    
    
}