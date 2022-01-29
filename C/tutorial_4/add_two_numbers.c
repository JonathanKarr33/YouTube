#include <stdio.h>

int main(){
    double num1, num2;
    printf("Enter two numbers to add: ");
    scanf(" %lf %lf", &num1, &num2);
    double sum = num1 + num2;
    printf("%g + %g = %g\n", num1, num2, sum);
    return 0;
}