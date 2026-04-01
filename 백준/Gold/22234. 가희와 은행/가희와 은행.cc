#include <iostream>
#include <queue>
#include <tuple>
#include <vector>
#include <functional>

using namespace std;

int main() {
    queue<pair<int, int>> waiting;
    priority_queue<
        tuple<int, int, int>,
        vector<tuple<int,int,int>>,
        greater<tuple<int,int,int>>
        > outside;
    
    int N, T, W, M;
    cin >> N >> T >> W;
    
    // Generate Waiting Queue
    for (int i = 0; i < N; i++) {
        int id, time;
        cin >> id >> time;
        waiting.push({id, time});
    }
    
    // Generate outside Queue
    cin >> M;
    for (int i = 0; i < M; i++) {
        int id, time, wait;
        cin >> id >> time >> wait;
        outside.push({wait, id, time});
    }
    
    // Start Process
    int clock = 0;
    while (clock < W) {
        auto [id, time] = waiting.front();
        waiting.pop();

        int work = min(time, T);

        for (int i = 0; i < work; i++) {
            cout << id << "\n";
            clock++;
            
            // Insert Outsider into waiting.
            while (!outside.empty()) {
                auto [o_wait, o_id, o_time] = outside.top();
                if (o_wait <= clock) {
                    waiting.push({o_id, o_time});
                    outside.pop();
                } else {
                    break;
                }
            }
            if (clock >= W) return 0;
        }
        // New Waiting
        if (time > T) {
            waiting.push({id, time - T});
        }
    }
    return 0;
}