#include <bits/stdc++.h>
using namespace std;
 
#define endl '\n'
#define REP(i, a, b) for (auto i = (a); i != (b); ++i)
 
template <typename Itr>
void Sort(Itr first, Itr last) {
    if (last - first < 2) return;
    auto pivot = *first;
    swap(*first, *(last - 1));
    Itr it = first;
    Itr pivit = first;
    for (; it != last; ++it) {
        if (*it < pivot) {
            swap(*it, *pivit);
            ++pivit;
        }
    }
    swap(*(last - 1), *pivit);
    Sort(first, pivit);
    Sort(pivit + 1, last);
}
 
int main() {
    int n;
    cin >> n;
    REP(i, 0, 1<<n) {
        int j = i ^ (i >> 1);
        for (int b = n - 1; b >= 0; b--) {
            putchar('0' + (bool)(j & (1 << b)));
        }
        putchar('\n');
    }
}
