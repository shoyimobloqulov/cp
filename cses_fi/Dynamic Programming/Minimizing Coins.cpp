#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int main() {
    int n, m;
    cin >> n >> m;
 
    vector<int> r(n); 
    for (int i = 0; i < n; i++) {
        cin >> r[i];
    }
 
    vector<int> dp(m + 1, 1e9); 
    dp[0] = 0; 
    for (int i = 1; i <= m; i++) {
        for (int j = 0; j < n; j++) {
            if (i - r[j] >= 0) {
                dp[i] = min(dp[i], dp[i - r[j]] + 1);
            }
        }
    }
    cout << (dp[m] != 1e9 ? dp[m] : -1) << endl;
 
    return 0;
}
