#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long p10(int n){
    int i, j;
    char *a;
    long sum = 0;
    a = alloca(sizeof(char) * n);
    memset(a, 1, n);
    a[1] = 1;
    for(i=2;i<n;i++){
        if(a[i]){
            for(j=i+i; j<n; j+=i){
                a[j] = 0;
            }
        }
    }
    for(i=2;i<n;i++){
        if(a[i]) sum += i;
    }

    return sum;
}

int main(int argc, char *argv[]){
    printf("%ld\n", p10(2000000));
    return EXIT_SUCCESS;
}
