#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int p2(int n){
    int sum=0, t;
    int a_1 = 1;
    int a = 1;
    while(a < n){
        if(a % 2 == 0){
            sum += a;
        }
        t = a + a_1;
        a_1 = a;
        a = t;
    };
    return sum;
}

int main(){
    printf("%d\n", p2(4000000));
    return EXIT_SUCCESS;
}
