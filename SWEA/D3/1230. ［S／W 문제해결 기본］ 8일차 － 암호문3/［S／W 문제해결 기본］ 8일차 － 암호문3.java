import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Solution {
    static LinkedList<String> passwordDummy;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= 10; tc++) {
            // init
            int N = Integer.parseInt(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            passwordDummy = new LinkedList<>();
            for (int i = 1; i <= N; i++) {
                passwordDummy.add(st.nextToken());
            }

            int M = Integer.parseInt(br.readLine());
            StringTokenizer commandDummy = new StringTokenizer(br.readLine());
            while (commandDummy.hasMoreTokens()) {
                String command = commandDummy.nextToken();
                if (command.equals("I")) {
                    int x = Integer.parseInt(commandDummy.nextToken());
                    int y = Integer.parseInt(commandDummy.nextToken());
                    String[] passwordList = new String[y];
                    for (int i = 0; i < y; i++) {
                        passwordList[i] = commandDummy.nextToken();
                    }
                    insert(x, passwordList);
                } else if (command.equals("D")) {
                    int x = Integer.parseInt(commandDummy.nextToken());
                    int y = Integer.parseInt(commandDummy.nextToken());
                    delete(x, y);
                } else {
                    int y = Integer.parseInt(commandDummy.nextToken());
                    String[] passwordList = new String[y];
                    for (int i = 0; i < y; i++) {
                        passwordList[i] = commandDummy.nextToken();
                    }
                    add(passwordList);
                }
            }
            sb.append("#" + tc + " ");
            for (int i = 1; i < 11; i++) {
                sb.append(passwordDummy.get(i) + " ");
            }
            sb.append("\n");
        }
        System.out.println(sb.toString().trim());

    }

    static void insert(int x, String[] passwordList) {
        for (String password : passwordList) {
            passwordDummy.add(++x, password);
        }
    }

    static void delete(int x, int y) {
        for (int i = 0; i < y; i++) {
            passwordDummy.remove(x++);
        }
    }

    static void add(String[] passwordList) {
        for (String password : passwordList) {
            passwordDummy.add(password);
        }
    }

}