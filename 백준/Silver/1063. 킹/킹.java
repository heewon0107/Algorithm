import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String first_king = st.nextToken();
        String first_rock = st.nextToken();
        // Hashmap 생성
        Map<Character, Integer> char_to_int = new HashMap<>();
        char_to_int.put('A', 0);
        char_to_int.put('B', 1);
        char_to_int.put('C', 2);
        char_to_int.put('D', 3);
        char_to_int.put('E', 4);
        char_to_int.put('F', 5);
        char_to_int.put('G', 6);
        char_to_int.put('H', 7);

        Map<Integer, Character> int_to_char = new HashMap<>();
        int_to_char.put(0, 'A');
        int_to_char.put(1, 'B');
        int_to_char.put(2, 'C');
        int_to_char.put(3, 'D');
        int_to_char.put(4, 'E');
        int_to_char.put(5, 'F');
        int_to_char.put(6, 'G');
        int_to_char.put(7, 'H');

        int r_king, c_king, r_rock, c_rock;

        c_king = char_to_int.get(first_king.charAt(0));
        r_king = Character.getNumericValue(first_king.charAt(1)) - 1;
        c_rock = char_to_int.get(first_rock.charAt(0));
        r_rock = Character.getNumericValue(first_rock.charAt(1)) - 1;

        // 보드 생성
        Character[][] board = new Character[8][8];
        board[r_king][c_king] = 'K';
        board[r_rock][c_rock] = 'R';
        int controlNum = Integer.parseInt(st.nextToken());
        for (int i = 0; i < controlNum; i++) {
            String way = br.readLine();
            int r = 0;
            int c = 0;

            switch (way) {
                case "R":
                    c = 1;
                    break;
                case "L":
                    c = -1;
                    break;
                case "B":
                    r = -1;
                    break;
                case "T":
                    r = 1;
                    break;
                case "RT":
                    r = 1;
                    c = 1;
                    break;
                case "RB":
                    r = -1;
                    c = 1;
                    break;
                case "LT":
                    r = 1;
                    c = -1;
                    break;
                case "LB":
                    r = -1;
                    c = -1;
                    break;
            }

            int nr, nc;
            nr = r_king + r;
            nc = c_king + c;
            // 범위 안이면 가자.
            if (0 <= nr && nr < 8 && 0 <= nc && nc < 8) {
                // 돌 이 아니고 빈공간.
                if (board[nr][nc] == null) {
                    board[nr][nc] = 'K';
                    board[r_king][c_king] = null;

                }

                // 돌이면 돌 범위 검사
                else if (board[nr][nc] == 'R') {
                    int nr_r = nr + r;
                    int nc_r = nc + c;
                    if (0 <= nr_r && nr_r < 8 && 0 <= nc_r && nc_r < 8) {
                        board[nr_r][nc_r] = 'R';
                        board[nr][nc] = 'K';
                        board[r_king][c_king] = null;
                        
                        r_rock = nr_r;
                        c_rock = nc_r;
                    }else { // 돌이 못움직이면 킹도 못움직임.
                        continue;
                    }
                }// 돌과 킹 이동 시 범위 안이면 킹 위치 변경
                r_king = nr;
                c_king = nc;

            }
        }
        String R = "";
        R += int_to_char.get(c_king);
        r_king ++;
        r_rock ++;
        String Rock = "";
        Rock += int_to_char.get(c_rock);
        System.out.println(R + r_king);
        System.out.println(Rock + r_rock);
        br.close();
    }

}
