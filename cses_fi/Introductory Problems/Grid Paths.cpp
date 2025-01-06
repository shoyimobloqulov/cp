#include <iostream>
#include <vector>
#include <string>

using namespace std;

int dx[] = {0, 0, 1, -1};
int dy[] = {1, -1, 0, 0};
string s;
int v[7][7] = {0};

int func(int x, int y, int p) {
    if (p == s.length()) {
        return (x == 6 && y == 0) ? 1 : 0;
    }
    if (x == 6 && y == 0) return 0;
    if (v[x][y]) return 0;

    int c[4] = {-1, -1, -1, -1};
    for (int k = 0; k < 4; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];
        if (nx >= 0 && nx < 7 && ny >= 0 && ny < 7) {
            c[k] = v[nx][ny];
        }
    }

    if (!c[2] && !c[3] && c[0] && c[1]) return 0;
    if (!c[0] && !c[1] && c[2] && c[3]) return 0;
    if (x - 1 >= 0 && y + 1 < 7 && v[x - 1][y + 1] == 1 && !c[0] && !c[3]) return 0;
    if (x + 1 < 7 && y + 1 < 7 && v[x + 1][y + 1] == 1 && !c[0] && !c[2]) return 0;
    if (x - 1 >= 0 && y - 1 >= 0 && v[x - 1][y - 1] == 1 && !c[1] && !c[3]) return 0;
    if (x + 1 < 7 && y - 1 >= 0 && v[x + 1][y - 1] == 1 && !c[1] && !c[2]) return 0;

    v[x][y] = 1;
    int r = 0;
    if (s[p] == '?') {
        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx >= 0 && nx < 7 && ny >= 0 && ny < 7) {
                r += func(nx, ny, p + 1);
            }
        }
    } else if (s[p] == 'R' && y + 1 < 7) {
        r += func(x, y + 1, p + 1);
    } else if (s[p] == 'L' && y - 1 >= 0) {
        r += func(x, y - 1, p + 1);
    } else if (s[p] == 'U' && x - 1 >= 0) {
        r += func(x - 1, y, p + 1);
    } else if (s[p] == 'D' && x + 1 < 7) {
        r += func(x + 1, y, p + 1);
    }
    v[x][y] = 0;
    return r;
}

int main() {
    cin >> s;
    cout << func(0, 0, 0) << endl;
    return 0;
}
