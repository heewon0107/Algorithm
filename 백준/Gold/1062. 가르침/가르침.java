import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, K, max = 0;
    static String[] words;
    static boolean[] learned = new boolean[26];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        words = new String[N];

        // 최소 필요한 문자 수
        if (K < 5) {
            System.out.println(0);
            return;
        }

        // 기본적으로 배우는 다섯 글자
        learned['a' - 'a'] = true;
        learned['c' - 'a'] = true;
        learned['i' - 'a'] = true;
        learned['n' - 'a'] = true;
        learned['t' - 'a'] = true;

        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            words[i] = word.substring(4, word.length() - 4); // "anta" 와 "tica" 제거
        }

        // 백트래킹 시작
        dfs(0, 0);
        System.out.println(max);
    }

    // start: 탐색 시작 위치, depth: 현재까지 배운 글자 수
    static void dfs(int start, int depth) {
        if (depth == K - 5) {
            int count = 0;
            for (String word : words) {
                boolean readable = true;
                for (int i = 0; i < word.length(); i++) {
                    if (!learned[word.charAt(i) - 'a']) {
                        readable = false;
                        break;
                    }
                }
                if (readable) count++;
            }
            max = Math.max(max, count);
            return;
        }

        for (int i = start; i < 26; i++) {
            if (!learned[i]) {
                learned[i] = true;
                dfs(i + 1, depth + 1);
                learned[i] = false;
            }
        }
    }
}
