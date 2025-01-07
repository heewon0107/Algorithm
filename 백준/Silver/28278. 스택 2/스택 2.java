import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        ArrayList<Integer> stack = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String input = br.readLine();
            String[] parts = input.split(" ");
            int order = Integer.parseInt(parts[0]);
            int num = 0;

            if (parts.length > 1) {
                num = Integer.parseInt(parts[1]);
            }

            switch (order) {
                case 1: // push
                    stack.add(num);
                    break;
                case 2: // pop
                    if (stack.isEmpty()) {
                        sb.append("-1").append("\n");
                    } else {
                        int pickNum = stack.remove(stack.size() - 1);
                        sb.append(pickNum).append("\n");
                    }
                    break;
                case 3: // size
                    sb.append(stack.size()).append("\n");
                    break;
                case 4: // empty
                    if (stack.isEmpty()) {
                        sb.append("1").append("\n");
                    } else {
                        sb.append("0").append("\n");
                    }
                    break;
                case 5: // top
                    if (stack.isEmpty()) {
                        sb.append("-1").append("\n");
                    } else {
                        sb.append(stack.get(stack.size() - 1)).append("\n");
                    }
                    break;
            }
        }

        System.out.print(sb.toString());
    }
}
