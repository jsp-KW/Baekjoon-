class Solution {
    int [] answer = new int[2];
    int[][] arr;
    
    void compress (int y, int x, int size) {
        if (check_same(arr,y,x,size)) {
            int val = arr[y][x];
            answer[val] +=1;
            return;
        }
        
        int half_size = size /2;
        
        compress (y,x,half_size);
        compress(y, x+half_size, half_size);
        compress(y+half_size, x, half_size);
        compress(y+half_size, x+half_size, half_size);
        
    }
    
    boolean check_same(int[][] arr,int y, int x, int size) {
        int first_val = arr[y][x];
        
        for (int i =y; i<y+size; i++) {
            for (int j = x; j<x+size; j++) {
                if (first_val != arr[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
    
    public int[] solution(int[][] arr) {
        this.arr = arr;
        compress(0,0,arr.length);
        
        
        return answer;
    }
}