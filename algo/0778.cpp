#include <bits/stdc++.h>

using namespace std;

long long mod = 1000000007;

long long gcd(long long a, long long b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

long long lcm(long long a, long b)
{
    return (a / gcd(a, b)) * b;
}

long long power(long long a, long long b, long long mod)
{
    long long result = 1;
    while (b > 0)
    {
        if (b % 2 == 1)
        {
            result = (result * a) % mod;
        }
        a = (a * a) % mod;
        b /= 2;
    }
    return result;
}

long long modInverse(long long a, long long mod)
{
    return power(a, mod - 2, mod);
}

long long check(long long x, long long n)
{
    long long m = n / x;
    long long result = (x % mod) * (m % mod) % mod;
    result = result * ((m + 1) % mod) % mod;
    result = result * modInverse(2, mod) % mod;
    return result;
}

int main()
{
    long long n, a, b;
    cin >> n >> a >> b;

    long long sa = check(a, n);
    long long sb = check(b, n);
    long long sab = check(lcm(a, b), n);

    long long res = (sa + sb - sab + mod) % mod;

    cout << res << endl;
    return 0;
}
