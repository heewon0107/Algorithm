import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        if (n == k) {
            System.out.println(0);
            return;
        }
        // 앞 자리 숫자가 커야 좋다.
        // k 갯수 만큼의 배열에 작은 수들을 스택하자.
        // 큰 숫 자가 앞에 있어야한다.
        // 큰 숫 자를

        // 다른 방안
        // 0번 째부터 순회하면서 스택 쌓고, 다음 수보다 크면 또 쌓아, 다음 수가 크면 sb에 붙이고 스택 비우고 k--
        LinkedList<Character> stack = new LinkedList<>();
        int index = 0;
        String num = br.readLine();
        stack.add(num.charAt(0));

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < num.length(); i++) {
            // 전 숫자가 더 작다.
            
            // 앞 숫자가 작으면 자리 바꿔주기
            if (stack.get(index) < num.charAt(i)) {
                stack.pollLast();
                k--;
                // 지울 횟수 남고, 스택이 남아 있으면. 이전 스택 확인해서 작은거 있으면 바꿔줌.
                while (k > 0 && index > 0 && !stack.isEmpty() && stack.get(index - 1) < num.charAt(i)) {
                    index--;
                    stack.pollLast();
                    k--;
                }
                stack.add(num.charAt(i));
            } else if (stack.get(index) >= num.charAt(i)) {
                index++;
                stack.add(num.charAt(i));
            }

            if (k == 0) {
                for (int j = i + 1; j < num.length(); j++) {
                    stack.add(num.charAt(j));
                }
                break;
            }
        }

        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        while (k > 0) {
            sb.deleteCharAt(sb.length() - 1);
            k--;
        }
        System.out.println(sb.toString());

    }
}
