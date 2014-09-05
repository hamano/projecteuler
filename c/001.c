#include <stdio.h>

int p1(int n){
    int s=0;
    do s += (n % 3 && n % 5)?0:n; while(n--);
    return s;
}

int main(){
    printf("%ld\n", p1(1000));
    return 0;
}
