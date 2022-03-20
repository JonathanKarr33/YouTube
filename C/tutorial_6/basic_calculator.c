/*********************************
Program: basic_calculator.c
Author: Jonathan Karr
This program is a basic calculator run in the terminal
*********************************/

#include <stdio.h>

int main(){
    double num1, num2;
    char op;
    printf("Enter a number, operator symbol, and another number: ");
    scanf("%lf %c %lf", &num1, &op, &num2);
    if(op == '+'){
        printf("%g + %g = %g\n", num1, num2, num1 + num2);
    }
    else if(op == '-'){
        printf("%g - %g = %g\n", num1, num2, num1 - num2);
    }
    else if(op == '*'){
        printf("%g * %g = %g\n", num1, num2, num1 * num2);
    }
    else if(op == '/'){
        printf("%g / %g = %g\n", num1, num2, num1 / num2);
    }
    else{
        printf("Invalid operator\n");
    }
    return 0;
}