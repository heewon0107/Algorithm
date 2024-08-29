#include <iostream>
#include <vector>
#include <cmath> // abs 함수 사용을 위한 헤더 파일

using namespace std;

int main() {
    int T;
    cin >> T;
    
    for (int tc = 1; tc <= T; ++tc) {
        int N;
        cin >> N;
        vector<int> arr(N);
        
        for (int i = 0; i < N; ++i) {
            cin >> arr[i];
        }
        
        int closer = 100000;
        int cnt = 0;
        
        for (int i = 0; i < N; ++i) {
            int absValue = abs(arr[i]);
            if (absValue < closer) {
                closer = absValue;
                cnt = 1;
            } else if (absValue == closer) {
                ++cnt;
            }
        }
        
        cout << "#" << tc << " " << closer << " " << cnt << endl;
    }
    
    return 0;
}
