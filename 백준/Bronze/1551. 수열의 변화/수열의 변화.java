import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 수열의 크기
        int k = Integer.parseInt(st.nextToken()); // 반복 횟수
        String s = br.readLine();
        String[] lst = s.split(",");
        int[] intArray = new int[n];
        for (int i = 0; i < n; i++) {
            intArray[i] = Integer.parseInt(lst[i].trim());
        }
        for (int i = 1; i < k+1; i++) {
            int[] new_list = new int[n-i]; // 한 칸 작은 리스트 만들기.
            for (int j = 0; j < n-i; j++) {
                new_list[j] = intArray[j+1] - intArray[j];
            }
            intArray = new_list;
        }
        for (int i = 0; i < intArray.length; i++) {
            System.out.print(intArray[i]);
            if (i != intArray.length - 1) {
                System.out.print(',');
            }
        }
        br.close();
    }

}
