#include <stdio.h>
int main(){
    int a = 7; // 0000 0111   2^2 + 2^1 + 2 ^0 = 4 + 2 + 1 =7
    int b = 6; // 0000 0110
    printf("and %d\n", a & b);
    printf("or %d\n", a | b);
    printf("xor %d\n", a ^ b);
    printf("not %d\n", ~a); //1111 1000    0000 1111   7+1=8
    printf("shift left %d\n", a << 1); // 0000 1110
    printf("shift right %d\n", a >> 1);// 0000 0011
    return 0;
}