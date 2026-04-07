#include <iostream>
#include <stack>

using namespace std;
stack<int> s;

int main(){
    int N;
    cin >> N;
    while (N--) {
        string cmd;
        int x;
        cin >> cmd;
        if (cmd == "push") {
            cin >> x;
            s.push(x);
        } else if (cmd == "pop") {
            if (s.empty()) {
                cout << -1 << "\n";
            } else {
                cout << s.top() << "\n";
                s.pop();
            }
        } else if (cmd == "size") {
            cout << s.size() << "\n";
        } else if (cmd == "empty") {
            if (s.empty()) cout << 1 << "\n";
            else cout << 0 << "\n";
            
        } else if (cmd == "top") {
            if (s.empty()) cout << -1 << "\n";
            else cout << s.top() << "\n";
        }
    }
    
    return 0;
}
