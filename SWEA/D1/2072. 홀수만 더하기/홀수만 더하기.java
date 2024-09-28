import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int t = scan.nextInt(); // 테스트 케이스 입력받기.

        for (int i = 1; i < t+1; i++) {
            int result = 0;
            int[] arr = new int[10];  // 10개의 정수를 입력받기.
            for (int j = 0; j <10; j++){
                int x = arr[i] = scan.nextInt();
                if (x % 2 == 1){
                    result += x;
                }

            }
            System.out.println("#" + i + " " + result);

        }
    }
}