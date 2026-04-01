#include <iostream>
#include <vector>
#include <cmath>
#include <queue>

using namespace std;

string bfs(int sx, int sy, vector<pair<int, int>> stores, int ex, int ey) {
    vector<int> visited(stores.size(), 0);
    
    queue<pair<int, int>> q;
    q.push({sx, sy});
    
    while (!q.empty()) {
        auto cur = q.front();
        q.pop();
        
        int x = cur.first;
        int y = cur.second;
        if (abs(x - ex) + abs(y - ey) <= 1000) {
            return "happy";
        }
        
        for (int i = 0; i < stores.size(); i++) {
            if (!visited[i]) {
                int nx = stores[i].first;
                int ny = stores[i].second;
                if (abs(x - nx) + abs(y - ny) <= 1000) {
                    visited[i] = 1;
                    q.push({nx, ny});              
                }
            }
        }
    }
    return "sad";
    
}

int main() {
    int T, N;
    cin >> T;
    for (int tc = 0; tc < T; tc++) {
        cin >> N;
        int sx, sy, ex, ey;
        cin >> sx >> sy;
        vector<pair<int, int>> stores;
        for (int n = 0; n < N; n++) {
            int x, y;
            cin >> x >> y;
            stores.push_back({x, y});
        }
        cin >> ex >> ey;
        cout << bfs(sx, sy, stores, ex, ey) << "\n";
    }
    return 0;
}