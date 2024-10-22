import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String firstNum = br.readLine();
        int[] arr = new int[firstNum.length()];
        for (int i = 0; i < firstNum.length(); i++) {
            arr[i] = firstNum.charAt(i) - '0';
        }
        for (int i = 0; i < firstNum.length() - 1; i++) {
            for (int j = i+1; j < firstNum.length(); j++) {
                if (arr[i] < arr[j]) {
                    int num = arr[i];
                    arr[i] = arr[j];
                    arr[j] = num;
                }
            }
        }
        for (int i : arr) {
            System.out.print(i);

        }
    }
}
