import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n, m;
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int result = 64;

        // Input Setting
        String[][] input = new String[n][m];
        for (int i = 0; i < n; i++) {
            input[i] = br.readLine().split("");
        }

        for (int i = 0; i < n-7; i++) {
            for (int j = 0; j < m-7; j++) {

                // Board Setting
                String[][] board = new String[8][8];
                for (int x = 0; x < 8; x++) {
                    for (int y = 0; y < 8; y++) {
                        board[x][y] = input[i + x][j + y];
                    }
                }

                String leftTop = input[i][j];
                int cnt = 0;
                // Same color Check
                for (int x = 0; x < 8; x++) {
                    for (int y = 0; y < 8; y++) {
                        if ((x + y) % 2 == 0) {
                            if (!board[x][y].equals(leftTop)) {
                                cnt++;

                            }
                        } else {
                            if (board[x][y].equals(leftTop)) {
                                cnt++;
                            }
                        }
                    }
                }
                result = Math.min(result, cnt);
                cnt = 0;

                // reverse color Check
                if (leftTop.equals("W")) {
                    leftTop = "B";
                } else {
                    leftTop = "W";
                }
                for (int x = 0; x < 8; x++) {
                    for (int y = 0; y < 8; y++) {
                        if ((x + y) % 2 == 0) {
                            if (!board[x][y].equals(leftTop)) {
                                cnt++;
                            }
                        } else {
                            if (board[x][y].equals(leftTop)) {
                                cnt++;
                            }
                        }
                    }
                }
                result = Math.min(result, cnt);

            }
        }
        System.out.println(result);

    }

}
