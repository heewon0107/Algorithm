#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;

    for (int i = 0; i < t; i++) {
        int num;
        cin >> num;
        if ((num + 1) % (num % 100) == false) {
            cout << "Good" << endl;
        } else {
            cout << "Bye" << endl;
        }
    }
    
    return 0;
}