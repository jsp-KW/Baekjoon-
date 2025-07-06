

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int people = sc.nextInt();
		
		int arr [] = new int[people];
		
		int time_result[] = new int[people];
		
		for (int i =0; i<people; i++) {
			
			arr[i] = sc.nextInt();
			
		}
		
	 // 오름차순 정리를 이용
		
		Arrays.sort(arr);
		
		
		/*
		 * for (int i =0; i<arr.length;i++) { System.out.println(arr[i]); }
		 */
		
		time_result[0] = arr[0];
		int temp = 0;

		for (int i=1; i<time_result.length;i++) {
			
			temp =time_result[i-1];
			time_result[i] = temp+arr[i];
		}
		
		int total =0 ;
		for (int i =0; i<time_result.length;i++) {
			
			total += time_result[i];
		}
	
		
		System.out.println(total);
	}

}
