#include "functions.h"

int main(){
    printf("Happy birthday you are 15\n");
    printf("Happy birthday you are 18\n");
    happy_birthday(15);
    happy_birthday(18);
    //printf("%d\n",age); undefined
    float val = 5;
    float cubed = cube(val);
    printf("%g cubed is %g\n",val, cubed);
    return 0;
}