import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N, K;
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        LinkedList<Integer> circle = new LinkedList<>();
        LinkedList<Integer> result = new LinkedList<>();

        for (int i = 1; i < N+1; i++) {
            circle.add(i);
        }
        int pick_man = 0;
        while (!circle.isEmpty()){
            pick_man = (pick_man + K - 1) % circle.size();
            result.add(circle.remove(pick_man)); // 원형 식탁에서 K 번째 사람 데려오기
        }
        System.out.print('<');
        for (int i = 0; i < result.size(); i++) {
            System.out.print(result.get(i));
            if (i == result.size()-1){
                continue;
            }
            System.out.print(", ");
        }
        System.out.print('>');
        br.close();
    }

}
