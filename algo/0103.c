#include <stdio.h>

int main() {
    int n, k, l;
    scanf("%d", &n);
    int nums[n];
    float avg = 0, sum = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d", &nums[i]);
    }

    scanf("%d", &k);
    scanf("%d", &l);

    for (int i = k - 1; i < l; i++) {
        sum += nums[i];
    }

    avg = sum / (l - k + 1);

    printf("%.1f", avg);

    return 0;
}
