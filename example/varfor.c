#include <stdio.h>

int main() {
    int s = 0, n;
    FILE *f = fopen("new.txt", "w");

    for (int i = 0; i < 5; i++) {
        scanf("%d", &n);
        s += n;
        fprintf(f, "%d%s", n, (i < 4) ? "+" : "=");
    }

    fprintf(f, "%d", s);
    fclose(f);
}
