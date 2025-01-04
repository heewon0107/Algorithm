import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] numbers = new int[10];
        int maxValue = 0;
        int maxIndex = 0;
        for (int i = 1; i < 10; i++) {
            numbers[i] = Integer.parseInt(br.readLine());
            if (numbers[i] > maxValue) {
                maxValue = numbers[i];
                maxIndex = i;
            }
        }
        System.out.println(maxValue);
        System.out.println(maxIndex);
    }
}
