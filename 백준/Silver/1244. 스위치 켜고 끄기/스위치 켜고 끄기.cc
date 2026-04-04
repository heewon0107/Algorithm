#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N;
    vector<int> switches(N+1, 0);
    for (int i = 1; i <= N; i++) {
        int x;
        cin >> x;
        switches[i] = x;
    }
    cin >> M;
    // O(100)
    while (M--) {
        int sex, num;
        cin >> sex >> num;
        // 남자 - 받은 수의 배수 변경 O(100)
        if (sex == 1) {
            int cnt;
            cnt = 1;

            while (num * cnt <= N) {
                switches[num * cnt] = (switches[num * cnt] + 1) % 2;
                cnt++;
            }
        }
        // 여자 - 좌우 대칭인 스위치 변경 O(50)
        else if (sex == 2) {
            // 중앙 변경
            switches[num] = (switches[num] + 1) % 2;
            int l, r;
            l = num - 1;
            r = num + 1;
            while (l > 0 && r <= N && switches[l] == switches[r]) {
                switches[l] = (switches[l] + 1) % 2;
                switches[r] = (switches[r] + 1) % 2;
                l--;
                r++;
            }
        }
    }
    for (int i=1; i<=N; i++) {
        cout << switches[i] << " ";
        if (i % 20 == 0) cout << "\n";
    }
    return 0;
}