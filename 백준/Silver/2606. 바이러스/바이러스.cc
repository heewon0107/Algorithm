#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> computers;
vector<int> visited;
int answer = 0;

void dfs(int node) {
    for (int next_node: computers[node]) {
        if (!visited[next_node]) {
            answer++;
            visited[next_node] = 1;
            dfs(next_node);
        }
    }
}
int main() {
    int N, M;
    cin >> N >> M;

    computers.resize(N+1);
    visited.resize(N+1, 0);
    visited[1] = 1;
    
    // 양방향 인접리스트 생성
    while (M--) {
        int s, e;
        cin >> s >> e;
        computers[s].push_back(e);
        computers[e].push_back(s);
    }
    
    dfs(1);
    cout << answer << "\n";
    
    return 0;
}