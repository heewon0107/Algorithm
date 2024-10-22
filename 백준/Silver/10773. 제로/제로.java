import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        LinkedList<Integer> list = new LinkedList<>();
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                list.removeFirst();
            }else {
                list.addFirst(num);
            }
        }
        int result = 0;
        for (Integer i : list) {
            result += i;
        }
        System.out.println(result);

    }
}
