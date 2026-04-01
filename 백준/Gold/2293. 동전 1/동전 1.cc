#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    
    // coins
    vector<int> coins(N, 0);
    for(int i = 0; i < N; i++) {
        cin >> coins[i];
    }
    // dp
    vector<int> dp(K+1, 0);
    dp[0] = 1;
    for (int j = 0; j < N; j++) {
        for (int i = coins[j]; i < K+1; i++) {
            dp[i] += dp[i - coins[j]];
        }
    }
    cout << dp[K] << "\n";
    return 0;
    
}