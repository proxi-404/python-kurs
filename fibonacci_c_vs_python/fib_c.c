# include <stdio.h>

unsigned long long fib(n){
    if (n == 0) return 0;
    if (n == 1) return 1;
    unsigned long long result = 0;
    int i = 2;
    unsigned long long last = 1;
    unsigned long long penultimate = 0;
    while (i <= n){
        result = last + penultimate;
        penultimate = last;
        last = result;
        ++ i;
    }
    return result;
    
}

int main(){
    for(int i=0;  i<100; ++i){
        for(int n=0; n<1000; ++n){
            unsigned long  res = fib(n);
            printf("%lu, ", res);
        }
    }
    printf("\n");
    return 0;
}
