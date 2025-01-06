#include <bits/stdc++.h>

using namespace std;
int main() {
    int n;
    cin >> n;

    vector<double>a(n);
    for(auto &x: a) cin >> x;

    double mx = a[0];

    for(auto &x: a) mx = max(mx,x);


    for(auto &x: a) {
        x = 1.0 * (x / mx) + 0.00001;
    } 
    cout << fixed << setprecision(2);
    for(auto y: a) {
        cout << y << " ";
    }
    return 0;
}