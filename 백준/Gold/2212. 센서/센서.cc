#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N, K;
    vector<int> sensors;
    cin >> N >> K;
    if (K >= N) {
        cout << 0 << "\n";
        return 0;
    }
    for (int i = 0; i < N; i++) {
        int distance;
        cin >> distance;
        sensors.push_back(distance);
    }
    sort(sensors.begin(), sensors.end(), [](int a, int b) {
        return a < b;
    });
    vector<int> distances;
    for (int i = 1; i < N; i++) {
        distances.push_back(sensors[i] - sensors[i - 1]);
    }
    sort(distances.begin(), distances.end());
    int total = 0;
    for (int i=0; i < distances.size() - (K - 1); i++) {
        total += distances[i];
    }
    cout << total << "\n";    
    return 0;
}