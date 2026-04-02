#include <iostream>
#include <vector>

using namespace std;

int main() {
    int T, N;
    cin >> T;
    while (T--) {
        long long result = 0;
        cin >> N;
        vector<int> price(N, 0);
        for (int i=0; i < N; i++) {
            int p;
            cin >> p;
            price[i] = p;
        }
        int max_price = price[price.size() - 1];
        for (int i = price.size() - 1; i >= 0; i--) {
            if (price[i] >= max_price) {
                max_price = price[i];
            } else {
                result += max_price - price[i];
            }
        }
        cout << result << "\n";
    }
    return 0;
}