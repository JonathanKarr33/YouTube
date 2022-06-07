#include <stdio.h>
int main(){
    float number[5] = {992, 33, 33.2, 1, 2};
    number[4] = 3;
    int i;
    for(i = 0; i < (sizeof(number)/sizeof number[0]); i++){
        printf("Element [%d] = %g\n",i,number[i]);
    }
    int n[10];
    for(i = 0; i < 10; i ++){
        n[i] = 100 + i;
        printf("Element [%d] = %d\n",i,n[i]);
    }
    return 0;
}