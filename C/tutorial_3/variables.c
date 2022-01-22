#include <stdio.h>

int main(){

    int a;
    a = 5;
    int b = 4;
    int sum = a + b;
    float decimal = 5.4;
    double another_decimal = 5.4;
    int int_and_float = a + decimal;
    char letter = 'a';
    //char name[] = "Jonathan";
    char name[9] = "Jonathan";
    printf("The value of a is %d.\n",a);
    printf("The sum is %d.\n",sum);
    printf("The value of the float is %g and the value of the double is %g\n", decimal, another_decimal);
    printf("The sum of int a and float decimal is: %f\n",a + decimal);
    printf("The sum of int a and float decimal is: %d\n", int_and_float);
    printf("The letter is %c\n", letter);
    printf("My name is %s\n", name);
    return 0;
}